from django.contrib import admin
from .models import Profile
from .models import Book

admin.site.register(Book)
admin.site.register(Profile)
