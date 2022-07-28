from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book, Category, Writer, Genre
from .forms import ReviewForm


class GenreYear:
    """Жанры и года выхода книг"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Book.objects.filter(draft=False).values("year")



# Create your views here.
class BooksView(GenreYear, ListView):
    """Список книг"""
    book = Book
    queryset = Book.objects.filter(draft=False)
    paginate_by = 1


class BookDetailView(GenreYear, DetailView):
    """Полное описание книги"""
    book = Book
    slug_field = "url"

 

class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())

class WriterView(GenreYear, DetailView):
    """Вывод информации о актере"""
    model = Writer
    template_name = 'book/writer.html'
    slug_field = "name"


class FilterBooksView(GenreYear, ListView):
    """Фильтр книг"""
    paginate_by = 2

    def get_queryset(self):
        queryset = Book.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class Search(ListView):
    """Поиск книг"""
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context