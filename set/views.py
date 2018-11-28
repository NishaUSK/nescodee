from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'set/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'set/book_detail.html', {'books': books})

def book_new(request):
    if request.method == "BOOK":
        form = BookForm(request.BOOK)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'set/book_edit.html', {'form': form})

def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "BOOK":
        form = BookForm(request.BOOK, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.published_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'set/book_edit.html', {'form': form})


# def company_list(request):
#     return render(request, 'set/company_list.html', {})
