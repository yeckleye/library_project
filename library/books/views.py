from django.shortcuts import render, redirect
from django.forms import ModelForm

from books.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'pages']

def get_book(book_id):
  return Book.objects.get(id=book_id)

def book_list(request):
    books = Book.objects.all()
    data = {'all_books': books}
    return render(request, 'books/book_list.html', data)

def book_view(request, book_id):
    book = get_book(book_id)
    data = {'book': book}
    return render(request, 'books/book_detail.html', data)

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form': form, 'new_or_edit': 'New'})

def book_update(request, book_id):
    book = get_book(book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books:book_list')
    return render(request, 'books/book_form.html', {'form' :form, 'new_or_edit': 'Edit'})

def book_delete(request, book_id):
    book = get_book(book_id)
    if request.method=='POST':
        book.delete()
        return redirect('books:book_list')
    return render(request, 'books/book_confirm_delete.html', {'object':book})