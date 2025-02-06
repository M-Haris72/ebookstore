from django.contrib import admin
from .models import Profile
from .models import Book
from .models import Category,Cart

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Cart)