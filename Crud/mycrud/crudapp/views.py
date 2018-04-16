from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Book
from .forms import BookForm

# Create your views here.
def crud_task(request):
    cruds = Book.objects.all()
    return render(request, 'crudapp/read.html', { 'cruds': cruds })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'crudapp/detail.html', {'book': book})

def create_book(request):
    # return render(request, 'crudapp/create.html', { })
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # book.author = request.user
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'crudapp/create.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'crudapp/create.html', { 'form': form })

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('crud_task')