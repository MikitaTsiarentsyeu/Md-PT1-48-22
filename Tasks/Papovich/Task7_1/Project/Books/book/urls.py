from django.urls import path

from . import views


urlpatterns = [
    path("", views.BooksView.as_view()),
    path("filter/", views.FilterBooksView.as_view(), name='filter'),
    path("<slug:slug>/", views.BookDetailView.as_view(), name= "book_detail"),
    path("search/", views.Search.as_view(), name='search'),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("writer/<str:slug>/", views.WriterView.as_view(), name="writer_detail"),

]