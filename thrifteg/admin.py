from django.contrib import admin

# Register your models here.
# thrifteg/admin.py
from django.contrib import admin
<<<<<<< HEAD
from .models import Item, Category

admin.site.register(Item)
admin.site.register(Category)
=======
from .models import Item, Category, Seller

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Seller)
>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718
