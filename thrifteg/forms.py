# thrifteg/forms.py
from django import forms
from .models import Seller, ProductImage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SellerRegistrationForm(forms.ModelForm):
    product_type = forms.CharField(max_length=100, required=True)
    product_description = forms.CharField(widget=forms.Textarea, required=True)
    identity_image = forms.ImageField(required=True)  # Seller's identity
    
    class Meta:
        model = Seller
        fields = ['name', 'email', 'phone_number', 'address', 'product_type', 'product_description', 'identity_image']

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    description = forms.CharField(max_length=255, required=False, help_text="Description of the image")
    
    class Meta:
        model = ProductImage
        fields = ['image', 'description']

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
