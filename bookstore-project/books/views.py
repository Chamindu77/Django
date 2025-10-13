from django.shortcuts import render, get_object_or_404
from books.models import Book
from django.http import Http404

# import json
# import os
 
# # Get the base directory of your project
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # Build the correct path to books.json
# books_path = os.path.join(BASE_DIR, 'books.json')

# # Open JSON file safely
# with open(books_path, encoding='utf-8') as f:
#     data = json.load(f)

def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):

    singleBook = get_object_or_404(Book, id=id)
    
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)

# def show(request, id):

#     singleBook = list()
#     for book in data:
#         if book['id'] == id:
#             singleBook = book

#     context = {'book': singleBook}
#     return render(request, 'books/show.html', context)

