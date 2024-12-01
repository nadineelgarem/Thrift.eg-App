from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Seller, ProductImage, Category, Checkout


class SellerRegistrationForm(forms.ModelForm):
    product_type = forms.CharField(
        max_length=100,
        required=True,
        label="Product Type",
        help_text="Type of products you intend to sell"
    )
    product_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your products'}),
        required=True,
        label="Product Description",
        help_text="Detailed description of your products"
    )
    identity_image = forms.ImageField(
        required=True,
        label="Identity Image",
        help_text="Upload an identity document"
    )

    class Meta:
        model = Seller  # This links the form to the Seller model
        fields = ['name', 'email', 'phone_number', 'address', 'store_name', 'product_type', 'product_description', 'identity_image']

class SellerRatingForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'placeholder': 'Rate 1-5'}),
        label="Rate the Seller"
    )
    feedback = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Provide feedback'}),
        label="Feedback"
    )

class ProductRatingForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Rate the Product (1-5)",
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    feedback = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Provide feedback (optional)'}),
        label="Feedback",
    )
    class Meta:
        model = Seller
        fields = ['name', 'email', 'phone_number', 'address', 'store_name', 'product_type', 'product_description', 'identity_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Your address'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your store name'}),
        }

# Checkout Form
class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['full_name', 'address', 'city', 'zip_code', 'phone_number', 'payment_method']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP Code'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }

# Product Image Form
class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        label="Product Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )
    description = forms.CharField(
        max_length=255,
        required=False,
        label="Image Description",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brief description of the image (optional)'}),
    )

    class Meta:
        model = ProductImage
        fields = ['image', 'description']

# Custom User Signup Form
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid email address'}),
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label="Phone Number",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your contact number'}),
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control', 'placeholder': 'Enter your address'}),
        required=False,
        label="Address",
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }
class ItemRatingForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'placeholder': 'Rate 1-5'}),
        label="Rate this item"
    )
# Filter Form for Item Search
class FilterForm(forms.Form):
    # Price range filters
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min Price'}),
        label="Minimum Price",
    )
    max_price = forms.DecimalField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Price'}),
        label="Maximum Price",
    )

    # Size filter
    size = forms.ChoiceField(
        required=False,
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Size",
    )

    # Color filter
    color = forms.ChoiceField(
        required=False,
        choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Color",
    )

    # Condition filter
    condition = forms.ChoiceField(
        required=False,
        choices=[('New', 'New'), ('Used', 'Used')],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Condition",
    )
