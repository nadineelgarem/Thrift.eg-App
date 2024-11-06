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
    path('add_to_wishlist/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('wishlist/', views.view_wishlist, name='view_wishlist'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    #path('cart/', views.cart, name='cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_from_wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]