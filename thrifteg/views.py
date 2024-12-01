from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .models import Item, CartItem, WishlistItem, Category, Seller, ProductImage, ChatMessage
from .forms import SellerRegistrationForm, ProductImageForm, FilterForm 
from .forms import CheckoutForm


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

    return render(request, 'mainpage.html', {
        'items': items,
        'new_items': new_items,
        'gender': gender,
        'category': category,
        'query': query,  # Pass the query back for the search bar
    })




# Seller Registration View
def register_seller(request):
    if request.method == "POST":
        # Initialize forms with POST and FILES data
        seller_form = SellerRegistrationForm(request.POST, request.FILES)
        product_image_form = ProductImageForm(request.POST, request.FILES)

        # Check if both forms are valid
        if seller_form.is_valid() and product_image_form.is_valid():
            # Save the seller form first
            seller = seller_form.save()

            # Save product image form but don't commit to DB yet
            product_image = product_image_form.save(commit=False)
            product_image.seller = seller  # Associate image with the seller
            product_image.save()

            # Redirect to the main page after saving
            return redirect('mainpage')
        else:
            # Debugging - Print errors to console for visibility
            print("Seller Form Errors:", seller_form.errors)
            print("Product Image Form Errors:", product_image_form.errors)
            messages.error(request, "Please fix the errors below.")
    else:
        # If GET request, initialize empty forms
        seller_form = SellerRegistrationForm()
        product_image_form = ProductImageForm()

    return render(request, 'register_seller.html', {
        'seller_form': seller_form,
        'product_image_form': product_image_form,
    })

def category_items(request, gender, category_name):
    # Fetch items by gender and category
    items = Item.objects.filter(category__name=category_name, category__gender=gender).distinct()
    filter_form = FilterForm(request.GET)

    # Apply filters
    if filter_form.is_valid():
        # Get the cleaned data
        min_price = filter_form.cleaned_data.get('min_price')
        max_price = filter_form.cleaned_data.get('max_price')
        size = filter_form.cleaned_data.get('size')
        color = filter_form.cleaned_data.get('color')
        condition = filter_form.cleaned_data.get('condition')

        # Apply price range filter
        if min_price:
            items = items.filter(price__gte=min_price)
        if max_price:
            items = items.filter(price__lte=max_price)

        # Apply size filter (if size is part of the Item model)
        if size:
            items = items.filter(size=size)

        # Apply color filter (if color is part of the Item model)
        if color:
            items = items.filter(color=color)

        # Apply condition filter (if condition is part of the Item model)
        if condition:
            items = items.filter(condition=condition)

    return render(request, 'category_items.html', {
        'items': items,
        'category_name': category_name,
        'gender': gender,
        'filter_form': filter_form,  # Pass the form to the template
    })



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
    total_price = sum(item.item.price * item.quantity for item in cart_items)  # Use item.item.price
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.item.price * item.quantity for item in cart_items)  # Calculate total price

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Save the checkout details
            checkout = form.save(commit=False)
            checkout.user = request.user
            checkout.total_price = total_price
            checkout.save()

            # Clear the cart after checkout
            cart_items.delete()

            messages.success(request, "Your order has been placed successfully!")
            return redirect('mainpage')  # Redirect to main page or order confirmation page
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

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

def chat_view(request, seller_id):
    # Fetch the seller and create a new or retrieve existing chat
    seller = get_object_or_404(Seller, id=seller_id)
    # Retrieve chat messages between the logged-in user and the selected seller
    chat_messages = ChatMessage.objects.filter(seller=seller, user=request.user)

    if request.method == 'POST':
        # Save the new message to the chat
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(user=request.user, seller=seller, message=message)
    
    return render(request, 'chat_view.html', {
        'seller': seller,
        'chat_messages': chat_messages
    })
def chat_with_seller(request):
    sellers = Seller.objects.all()
    return render(request, 'chat_with_seller.html', {'sellers': sellers})

from django.shortcuts import render
from .models import Item

def search_results(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(category__name__icontains=query)
    else:
        items = Item.objects.all()
    return render(request, 'search_results.html', {'items': items, 'query': query})

from django.shortcuts import render, get_object_or_404
from .models import Item

def item_details(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return render(request, '404.html')  # Or another error page
    return render(request, 'item_details.html', {'item': item})

def filter_items(request):
    # Initialize filter form
    filter_form = FilterForm(request.GET)
    items = Item.objects.all()  # Default to all items

    # If the form is valid and filters are provided, apply them
    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        min_price = filter_form.cleaned_data.get('min_price')
        max_price = filter_form.cleaned_data.get('max_price')

        if category:
            items = items.filter(category=category)
        if min_price:
            items = items.filter(price__gte=min_price)
        if max_price:
            items = items.filter(price__lte=max_price)

    return render(request, 'mainpage.html', {
        'items': items,
        'filter_form': filter_form,
    })