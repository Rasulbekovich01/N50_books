from tkinter.tix import Form
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from models import Book, Author
from forms import Book, Form

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookCreateView(CreateView):
    model = Book
    form_class = Book , Form
    template_name = 'books/book_form.html'
    success_url = '/books/'

class BookUpdateView(UpdateView):
    model = Book
    form_class = Book, Form
    template_name = 'books/book_form.html'
    success_url = '/books/'

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = '/books/'

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
