from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    store_name = models.CharField(max_length=100)
    other_details = models.TextField(blank=True, null=True)
<<<<<<< HEAD

    def __str__(self):
        return self.name
=======
    rating = models.FloatField(default=0.0)  # Average rating
    num_ratings = models.PositiveIntegerField(default=0)  # Total number of ratings


    def __str__(self):
        return self.name
from django import forms

class RateSellerForm(forms.Form):
    seller_id = forms.IntegerField(widget=forms.HiddenInput())  # Hidden field to identify the seller
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 6)],  # 1 to 5 stars
        widget=forms.RadioSelect,
        label="Rate the seller"
    )
>>>>>>> partner-repo/main
