from django.shortcuts import render

# Create your views here.

from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Children genre (status = 'children')
    genre_children = Genre.objects.filter(name__exact='children').count()

    # Book with Title Drive (status = 'children')
    book_drive = Book.objects.filter(title__icontains='drive').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'genre_children': genre_children,
        'book_drive': book_drive,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
