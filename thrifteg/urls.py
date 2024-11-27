from django.urls import path
from . import views



#url config
urlpatterns = [
    path('', views.home, name='home'), 
    path('test/', views.test, name='test'),  
    path('signup/', views.signup, name='signup'),  
    path('login/',views.login,name='login') ,
    path('mainpage/', views.mainpage, name='mainpage'),  
#]

##---------------------------------------
    path('chat/', views.chat_with_seller, name='chat_with_seller'),
    path('chat/<int:seller_id>/', views.chat_view, name='chat_view'),

    path('search/', views.search_results, name='search_results'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),

    path('filter/', views.filter_items, name='filter_items'),

    path('add_to_wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    #path('cart/', views.cart, name='cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
      # Seller registration
    path('register_seller/', views.register_seller, name='register_seller'),
    

    path('category/<str:gender>/<str:category_name>/', views.category_items, name='category_items'),
    # Category view by name
    path('category/<str:category_name>/', views.category_items, name='category_items'),
]

