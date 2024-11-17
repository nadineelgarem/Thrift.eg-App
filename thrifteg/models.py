
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10,
        choices=[('Women', 'Women'), ('Men', 'Men'), ('Kids', 'Kids')]
    )
=======
    name = models.CharField(max_length=100)  # Example field for category name
    gender = models.CharField(max_length=10, choices=[('Women', 'Women'), ('Men', 'Men')])  # Example field for gender

    def __str__(self):
        return self.name  # This will display the category name in the admin panel

>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718

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
<<<<<<< HEAD
=======
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    store_name = models.CharField(max_length=100)
    other_details = models.TextField(blank=True, null=True)
    product_type = models.CharField(max_length=100, default="Not specified")  # Add default value
    product_description = models.TextField(default="No description provided")  # Add default text
    identity_image = models.ImageField(upload_to='identity/', default='default.jpg')

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.seller.name}"
>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return f"{self.user.username}'s Cart - {self.item.name} (x{self.quantity})"