from django.contrib import admin
from .models import *


admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(AuditLog)
admin.site.register(Discount)
admin.site.register(Wishlist)
admin.site.register(ShippingAddress)