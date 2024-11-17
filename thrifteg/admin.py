from django.contrib import admin

# Register your models here.
# thrifteg/admin.py
from django.contrib import admin
from .models import Item, Category, Seller

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Seller)