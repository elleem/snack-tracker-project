from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    template_name = "book_list.html"
    model = Book
    context_object_name = "books"


class BookDetailView(DetailView):
    template_name = "book_detail.html"
    model = Book


