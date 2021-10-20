from django.shortcuts import render
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import re
import datetime
 
from django.db.models import Q
 

def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    template_name = 'store/book_detail.html'
    context = {
        'book': None, # set this to an instance of the required book
        'num_available': None, # set this to the number of copies of the book available, or 0 if the book isn't available
        'your_rating': 'You have not yet rated this book',
    }
    # START YOUR CODE HERE
    context['book'] = Book.objects.get(id__exact=bid)
    list = BookCopy.objects.filter(Q(book=Book.objects.get(id__exact=bid)) & Q(available=True))
    count = list.count()
    context['num_available'] = count
    if request.user.is_authenticated:
        rate = Review.objects.filter(Q(book_reviewed=Book.objects.get(id__exact=bid)) & Q(reviewer=request.user))
        if rate.count()>0:
            x=rate[0].rating
            context['your_rating']=x
    
    
    return render(request, template_name, context=context)


@csrf_exempt
def bookListView(request):
    template_name = 'store/book_list.html'
    context = {
        'books': None, # set this to the list of required books upon filtering using the GET parameters
                       # (i.e. the book search feature will also be implemented in this view)
    }
    get_data = request.GET
    print(get_data)
    # START YOUR CODE HERE
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    genre = request.GET.get('genre', '')
    context['books'] = Book.objects.filter(
            Q(title__icontains=title) & Q(author__icontains=author) & Q(genre__icontains=genre))
    
    return render(request, template_name, context=context)

@login_required
def viewLoanedBooks(request):
    template_name = 'store/loaned_books.html'
    context = {
        'books': None,
    }
    '''
    The above key 'books' in the context dictionary should contain a list of instances of the 
    BookCopy model. Only those book copies should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE
    context['books'] = BookCopy.objects.filter(borrower=request.user)
    return render(request, template_name, context=context)

@csrf_exempt
@login_required
def loanBookView(request):
    response_data = {
        'message': None,
    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set the message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
    book_id = request.POST.get('bid') # get the book id from post data
    list = BookCopy.objects.filter(Q(book=Book.objects.get(id__exact=book_id)) & Q(available=True))
    count = list.count()
    if count>0:
        b=BookCopy.objects.filter(Q(book=Book.objects.get(id__exact=book_id)) & Q(available=True))[0]
        b.available=False
        b.borrower=request.user
        b.borrow_date=datetime.date.today()
        b.save()
        response_data['message'] = 'success'
    else:
        response_data['message'] = 'failure'
    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
''' 
@csrf_exempt
@login_required
def returnBookView(request):
    response_data = {
        'message': None,
    }
    print(request.POST.get('cid'))
    copy_id = request.POST.get('cid')
    c=BookCopy.objects.get(id__exact=copy_id)
    c.borrow_date=None
    c.available=True
    c.borrower=None
    c.save()
    response_data['message'] = 'success'
    return JsonResponse(response_data)

@csrf_exempt
@login_required
def rateBookView(request):
    response_data = {
        'message': None,
    }
    
    book_id = request.POST.get('bid')
    rateing = float(request.POST.get('brate'))
    list_book = Review.objects.filter(book_reviewed=Book.objects.get(id__exact=book_id))
    list_user_book = Review.objects.filter(Q(book_reviewed=Book.objects.get(id__exact=book_id)) & Q(reviewer=request.user))
    if len(list_user_book)==0:
        b=Book.objects.get(id__exact=book_id)
        b.rating=((b.rating*len(list_book))+rateing)/(len(list_book)+1)
        b.save()
        c=Review(book_reviewed=Book.objects.get(id__exact=book_id), rating=rateing, reviewer=request.user)
        c.save()
    else:
        c=Review.objects.filter(Q(book_reviewed=Book.objects.get(id__exact=book_id)) & Q(reviewer=request.user))[0]
        previous_rating_by_user = c.rating
        c.rating = rateing
        c.save()
        b = Book.objects.get(id__exact=book_id)
        previous_rating_of_book = b.rating
        new_rating = ((previous_rating_of_book*len(list_book))-previous_rating_by_user+rateing)/len(list_book)
        b.rating=new_rating
        b.save()

    response_data['message'] = 'success'
    return JsonResponse(response_data)
