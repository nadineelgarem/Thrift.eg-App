from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Seller, ProductImage
from .models import Category 
from .models import Checkout

# Seller Registration Form
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
        model = Seller
        fields = ['name', 'email', 'phone_number', 'address', 'store_name', 'product_type', 'product_description', 'identity_image']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['full_name', 'address', 'city', 'zip_code', 'phone_number', 'payment_method']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
        }
# Product Image Form
class ProductImageForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        label="Product Image",
        help_text="Upload an image for your product"
    )
    description = forms.CharField(
        max_length=255,
        required=False,
        label="Image Description",
        help_text="Provide a brief description of the image (optional)"
    )

    class Meta:
        model = ProductImage
        fields = ['image', 'description']

# Custom User Signup Form
class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        help_text="Enter a valid email address"
    )
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label="Phone Number",
        help_text="Provide your contact number"
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter your address'}),
        required=False,
        label="Address",
        help_text="Your address (optional)"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

class FilterForm(forms.Form):
    # Price range filters
    min_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'filter-input', 'placeholder': 'Min Price'}),
        min_value=0,
        label="Minimum Price"
    )
    max_price = forms.DecimalField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'filter-input', 'placeholder': 'Max Price'}),
        min_value=0,
        label="Maximum Price"
    )

    # Size filter
    size = forms.ChoiceField(
        required=False,
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')],
        widget=forms.Select(attrs={'class': 'filter-select'}),
        label="Size"
    )

    # Color filter
    color = forms.ChoiceField(
        required=False,
        choices=[('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Black', 'Black')],
        widget=forms.Select(attrs={'class': 'filter-select'}),
        label="Color"
    )

    # Condition filter
    condition = forms.ChoiceField(
        required=False,
        choices=[('New', 'New'), ('Used', 'Used')],
        widget=forms.Select(attrs={'class': 'filter-select'}),
        label="Condition"
    )

