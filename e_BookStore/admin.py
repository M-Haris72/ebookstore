from django.contrib import admin
from .models import *

# # Unregister first (to force Django to reload)
# admin.site.unregister(Book)
# admin.site.unregister(Category)

# Customize Book Admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'category', 'stock', 'created_at')  # Display these columns
    search_fields = ('title', 'author')  # Add a search box for books
    list_filter = ('category', 'author')  # Add filters in sidebar
    ordering = ('-created_at',)  # Show latest books first

# Customize Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(AuditLog)
admin.site.register(Discount)
admin.site.register(Wishlist)
admin.site.register(ShippingAddress)