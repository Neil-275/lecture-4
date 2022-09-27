from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/hello.html")

def login_view(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user= authenticate(request,username=username,password=password)
        if not user is None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html",{
                "mess":"We don't know you"
            })
    return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{
        "mess":"See you again"
    })