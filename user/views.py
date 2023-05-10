from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.contrib.auth.hashers import make_password





# Create your views here.

def user_register(request):
    
    #method 2:
    form = RegisterForm(request.POST or None)
    if form.is_valid(): 
    #calls the clean() method contained in the forms.py then get the credentials to create a user
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
                
        #create a new user
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
                
        #login the newuser and redirect to the home page
        login(request,newUser)
        messages.success(request, "Registered successfully...")
        
        return redirect("index")
    else:
        context = {
            "form": form,
        }
        return render(request, "register.html", context)
    
    
    """
    #methode 1: very complicated method.
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            #calls the clean() method contained in the forms.py then get the credentials to create a user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password ")
            
            #create a new user
            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            
            #login the newuser and redirect to the home page
            login(request,newUser)
            return redirect("index")
        else:
            context = {
                
                "form": form,
                
            }
            return render(request, "register.html", context)
    else: 
        form = RegisterForm()
        
        context = {
            "form": form,
        }
        return render(request, "register.html", context) """
    
    
def user_login(request):
    
    form = LoginForm(request.POST or None)
    
    context = {
        "form": form,
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            messages.success(request, f"Welcome Back {username}")
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or Password is not valid")
            return render(request, "login.html", context) 
    else:
        return render(request, "login.html", context)
   
    
def user_logout(request):
    logout(request)
    messages.success(request, "User logged out")
    return redirect("index")