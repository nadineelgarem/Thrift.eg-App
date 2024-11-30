from django.db import models
from django.contrib.auth.models import User

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)  # Example field for category name
    gender = models.CharField(
        max_length=10,
        choices=[('Women', 'Women'), ('Men', 'Men')],
        help_text="Target gender for the category"
    )

    def __str__(self):
        return f"{self.name} ({self.gender})"

# Item Model
class Item(models.Model):
    name = models.CharField(max_length=100)  # Add a name field for items
    category = models.ForeignKey(
        Category,  # Link to the Category model
        on_delete=models.CASCADE,  # Delete items if the category is deleted
        related_name='items'  # Allow reverse lookup from Category to Item
    )
    color = models.CharField(max_length=20, null=True, blank=True)
    condition = models.CharField(
        max_length=10,
        choices=[('New', 'New'), ('Used', 'Used')],
        null=True,
        blank=True,
    )
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="items/")
    date_added = models.DateTimeField(auto_now_add=True)
    is_new = models.BooleanField(default=True)

    def get_sizes_list(self):
        return self.available_sizes.split(",") if self.available_sizes else []

    def __str__(self):
        return self.name


# WishlistItem Model
class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='wishlist_entries')

    def __str__(self):
        return f"{self.user.username}'s Wishlist - {self.item.name}"

# Seller Model
class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    store_name = models.CharField(max_length=100)
    other_details = models.TextField(blank=True, null=True)
    product_type = models.CharField(max_length=100, default="Not specified")
    product_description = models.TextField(default="No description provided")
    identity_image = models.ImageField(upload_to='identity/', default='default.jpg')

    rating = models.FloatField(default=0.0)  # Average rating
    num_ratings = models.PositiveIntegerField(default=0)  # Number of ratings

    def __str__(self):
        return self.name

# ProductImage Model
class ProductImage(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='products/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.seller.name}"

# CartItem Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='cart_entries')
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, blank=True, null=True)  # Add this field

    def __str__(self):  # Ensure correct indentation
        return f"{self.item.name} (Size: {self.size}) x {self.quantity}"

# ChatMessage Model
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.user.username} to {self.seller.name} at {self.timestamp}"
