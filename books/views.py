from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Books
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db.models import Q

# Create your views here.
class BooksListView(LoginRequiredMixin,ListView):
    model = Books
    template_name = "books/books_list.html"
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView): # new
    model = Books
    template_name = "books/book_detail.html"
    context_object_name = "book" # new
    login_url = 'account_login'
    permission_required = 'books.special_status'
    queryset = Books.objects.all().prefetch_related('reviews__auther',)
    # all the reviews for each author in one go
  
class SearchResultsListView(ListView):
    model = Books
    template_name = 'books/search_results.html'
    context_object_name = 'book_list'
    # queryset = Books.objects.filter(title__icontains = "Professionals")
    # contains (which is case sensitive) or icontains197 (which is not case sensitive)

    def get_queryset(self):
        #  The last step is to take the user’s search query,
        #  represented by q in the URL,
        #  and pass it in to the actual search filters.
        query = self.request.GET.get("q")
        return Books.objects.filter(
            Q(title__icontains = query) | Q(author__icontains = query)
        )


