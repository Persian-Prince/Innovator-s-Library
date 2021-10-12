from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q


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