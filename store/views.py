from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from store.models import *


# Create your views here.


def index(request):
    return render(request, 'store/index.html')

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
            Q(titleicontains=title) & Q(authoricontains=author) & Q(genre__icontains=genre))

    return render(request, template_name, context=context) 


def bookDetailView(request, bid):
    template_name = 'store/book_detail.html'
    context = {
        'book': None,  # set this to an instance of the required book
        # set this to the number of copies of the book available, or 0 if the book isn't available
        'num_available': None,
        'your_rating': 'You have not yet rated this book',
    }
    # START YOUR CODE HERE
    context['book'] = Book.objects.get(id__exact=bid)
    list = BookCopy.objects.filter(
        Q(book=Book.objects.get(id__exact=bid)) & Q(available=True))
    count = list.count()
    context['num_available'] = count
    if request.user.is_authenticated:
        rate = Review.objects.filter(
            Q(book_reviewed=Book.objects.get(id__exact=bid)) & Q(reviewer=request.user))
        if rate.count() > 0:
            x = rate[0].rating
            context['your_rating'] = x

    return render(request, template_name, context=context)
