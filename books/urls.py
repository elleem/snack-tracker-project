from django.urls import path
from .views import BookListView, BookDetailView, AboutView


urlpatterns = [
    path('', BookListView.as_view(), name= 'book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('about', AboutView.as_view(), name='about'),
]