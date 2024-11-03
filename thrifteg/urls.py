from django.urls import path
from . import views

#url config
urlpatterns = [
    path('', views.home, name='home'), 
    path('test/', views.test, name='test'),  
    path('signup/', views.signup, name='signup'),  
    path('login/',views.login,name='login') ,
]