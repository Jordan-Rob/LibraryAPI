from django.shortcuts import render

from django.generic.views import ListView, DetailView

from .models import Book


# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'booklist.html'
