from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='book.all'),
    path('', views.BookListView.as_view(), name='book.all'),
    #path('<int:id>', views.show, name='book.show'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book.show'),
    path('<int:id>/review', views.review, name='book.review'),
    path('<str:author>', views.author, name='author.books'),
]

