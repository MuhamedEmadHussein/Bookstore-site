from django.urls import path
from .views import BooksListView,BookDetailView,SearchResultsListView

urlpatterns = [
    path("",BooksListView.as_view(),name="books_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
