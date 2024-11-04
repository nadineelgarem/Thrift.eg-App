from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

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
            return redirect("home")#change to successive page when created
    else:
        form = UserCreationForm()  #empty form
    return render(request, 'signup.html', {"form": form}) 
def login(request):
    return HttpResponse("login page")
def mainpage(request):
    return render(request, 'mainpage.html') 
