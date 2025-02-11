from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Book, Category  # Import models

def home(request):
    categories = Category.objects.all()  # Fetch all categories
    books_by_category = {category: Book.objects.filter(category=category)[:4] for category in categories}  
    # Fetch 4 books per category

    return render(request, 'index.html', {'books_by_category': books_by_category})




def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

from django.shortcuts import render
from .models import Book, Category

def store(request):
    category_id = request.GET.get('category')  # Get category from URL
    if category_id:
        books = Book.objects.filter(category_id=category_id)
    else:
        books = Book.objects.all()
    
    categories = Category.objects.all()  # Get all categories

    return render(request, 'store.html', {'books': books, 'categories': categories})
