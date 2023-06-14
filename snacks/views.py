from django.views.generic import ListView
from .models import Snack

class SnackListView(ListView):
    template_name = "book_list.html"
    model = Snack
    context_object_name = "books"


