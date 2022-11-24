from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book

# Create your views here.
def home(request):
    return render(request, "home.html")

def list(request):
    books = Book.objects.all()
    return render(request, "books-list.html", {"books": books})

def show(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "show.html", {"book": book})
