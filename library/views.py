from django.shortcuts import render, redirect, get_list_or_404
from .models import Library
from .forms import Libraryform

def home(request):
    books = Library.objects.all()
    return render(request, 'home.html', context={'books': books})

def detail_book(request, pk):
    book = get_list_or_404(Library, pk)
    return render(request, 'book.html', context={'book': book})

def create_book(request):
    libraryform = Libraryform()
    if request.method == 'POST':
        libraryform = Libraryform(request.POST)
        if libraryform.is_valid():
            libraryform.save()
            return redirect('home')     
    return render(request, 'create.html', context={'form': libraryform})

