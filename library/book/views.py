from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def books_filter(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(name__icontains=query)
    return render(request, 'books_list.html', {'books': books})

from django.shortcuts import render, get_object_or_404
from .models import Book 
from authentication.models import CustomUser
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    return user.role == 1 

@user_passes_test(is_librarian)
def books_by_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    books = Book.objects.filter(authors__id=user.id)
    return render(request, 'books_by_user.html', {'user': user, 'books': books})
