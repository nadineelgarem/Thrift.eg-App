from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse("signup page")
def login(request):
    return HttpResponse("login page")
