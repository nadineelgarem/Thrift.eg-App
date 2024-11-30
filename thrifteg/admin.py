from django.contrib import admin

# Register your models here.
# thrifteg/admin.py
from django.contrib import admin
from .models import Item, Category, Seller, ProductImage
<<<<<<< HEAD
=======
from .models import CartItem
>>>>>>> partner-repo/main

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(ProductImage)
<<<<<<< HEAD
=======
admin.site.register(CartItem)
>>>>>>> partner-repo/main
