
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('Women', 'Women'), ('Men', 'Men'), ('Kids', 'Kids')]
    )

    def _str_(self):
        return f"{self.name} ({self.gender})"

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Discounted price if applicable")
    stock_quantity = models.PositiveIntegerField(default=0, help_text="Number of items available in stock")
    image = models.ImageField(upload_to='items/')
    date_added = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    def _str_(self):
        return self.name

    @property
    def is_in_stock(self):
        return self.stock_quantity > 0

    @property
    def current_price(self):
        return self.discount_price if self.discount_price else self.price

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.user.username}'s Wishlist - {self.item.name}"

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return f"{self.user.username}'s Cart - {self.item.name} (x{self.quantity})"