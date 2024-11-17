<<<<<<< HEAD
=======

>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .models import Item, CartItem, WishlistItem  
=======
from django.forms import modelformset_factory
from .models import Item, CartItem, WishlistItem, Category, Seller, ProductImage
from .forms import SellerRegistrationForm, ProductImageForm

>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718


# Create your views here.
#request handler
#views functions take requests->response
#request handler
#functions take a request object and return response
#need to be mapped to URL

def test(request):
    return HttpResponse("testback")
def home(request):
    return render(request,'home.html')
def signup(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserCreationForm()  #empty form
    return render(request, 'signup.html', {"form": form}) 
#def login(request):
    #return HttpResponse("login page")
#def mainpage(request):
 #   return render(request, 'mainpage.html') 
def cart(request):
    return render(request, 'cart.html')
def wishlist(request):
    return render(request, 'wishlist.html')
##-------------------------------------------
def mainpage(request):
<<<<<<< HEAD
    gender = request.GET.get('gender', 'Women')
    category = request.GET.get('category')
    items = Item.objects.filter(category__gender=gender)
    if category:
        items = items.filter(category__name=category)
    new_items = Item.objects.filter(category__gender=gender, is_new=True).order_by('-date_added')[:10]
=======
    gender = request.GET.get('gender', 'Women')  # Default to 'Women'
    category = request.GET.get('category')      # Category from query parameters
    query = request.GET.get('query')            # Search query

    # Fetch all items for the selected gender
    items = Item.objects.filter(category__gender=gender).distinct()

    # Filter by category if specified
    if category:
        items = items.filter(category__name=category)

    # Filter by search query if specified
    if query:
        items = items.filter(name__icontains=query)

    # Fetch "new items" separately and exclude them from the general items list
    new_items = Item.objects.filter(category__gender=gender, is_new=True).distinct().order_by('-date_added')
    items = items.exclude(id__in=new_items.values_list('id', flat=True))  # Exclude new items from the general list

>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718
    return render(request, 'mainpage.html', {
        'items': items,
        'new_items': new_items,
        'gender': gender,
        'category': category,
<<<<<<< HEAD
    })

=======
        'query': query,  # Pass the query back for the search bar
    })




# Seller Registration View
def register_seller(request):
    ProductImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=3)
    if request.method == "POST":
        seller_form = SellerRegistrationForm(request.POST, request.FILES)
        formset = ProductImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())
        if seller_form.is_valid() and formset.is_valid():
            seller = seller_form.save()
            for form in formset:
                if form.cleaned_data:
                    product_image = form.save(commit=False)
                    product_image.seller = seller
                    product_image.save()
            return redirect('mainpage')
    else:
        seller_form = SellerRegistrationForm()
        formset = ProductImageFormSet(queryset=ProductImage.objects.none())
    return render(request, 'register_seller.html', {'seller_form': seller_form, 'formset': formset})

def category_items(request, gender, category_name):
    # Fetch items by gender and category
    items = Item.objects.filter(category__name=category_name, category__gender=gender).distinct()

    return render(request, 'category_items.html', {  # Ensure correct template is used
        'items': items,
        'category_name': category_name,
        'gender': gender,
    })



>>>>>>> eaabd58cb99ad6984355f8df90e7838729ec6718
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('mainpage')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.item.current_price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, f"Updated {item.name} quantity in your cart.")
    else:
        messages.success(request, f"Added {item.name} to your cart.")
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, user=request.user, item_id=item_id)
    cart_item.delete()
    messages.success(request, f"Removed {cart_item.item.name} from your cart.")
    return redirect('view_cart')

@login_required
def add_to_wishlist(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, item=item)
    if created:
        messages.success(request, f"Added {item.name} to your wishlist.")
    else:
        messages.info(request, f"{item.name} is already in your wishlist.")
    return redirect('view_wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, user=request.user, item_id=item_id)
    wishlist_item.delete()
    messages.success(request, f"Removed {wishlist_item.item.name} from your wishlist.")
    return redirect('view_wishlist')
