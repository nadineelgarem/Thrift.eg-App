from django.contrib import admin

# Register your models here.
# thrifteg/admin.py
from django.contrib import admin
from .models import Item, Category, Seller, ProductImage
from .models import Checkout

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(ProductImage)
admin.site.register(Checkout)
