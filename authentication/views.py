from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm , LoginForm



# Create your views here.

def login_view(request): 
    if request.user.is_authenticated:
        return redirect("/check_in/")
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid(): 
            print(form.data["email"], form.data["password"])
            user = authenticate(request, username = form.data["email"].strip(), password = form.data['password'].strip())
            print(user)
            if user is not None:
                login(request, user)
        return redirect('/check_in/')

    return render(request,"login.html")

def logout_view(request): 
    logout(request)
    return redirect("/login")
    

def register(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() 
        return redirect ("/login/")
    return render(request,"register.html")


