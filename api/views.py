from django.shortcuts import render

from rest_framework import generics

from books.models import Book


# Create your views here.
class BookAPIview(generics.ListAPIView):
