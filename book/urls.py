from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from book import views

urlpatterns = [
    path("books/", views.BookList.as_view()),
    path("books/<int:pk>/", views.BookDetail.as_view()),
    path("categories/", views.CategoryList.as_view()),
    path("categories/<int:pk>/", views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
