from django.shortcuts import render, HttpResponse
from .models import Book, Author

# Create your views here.
# def index(request):
#     return HttpResponse("Books app")


def index(request):
    # eqv.  SELECT * FROM books
    all_books = Book.objects.all()
    return render(request, 'books/index.template.html', {
        'books': all_books
    })


def view_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/authors.template.html', {
        'authors': all_authors
    })
