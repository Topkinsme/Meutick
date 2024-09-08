from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,"mainpage/dashboard.html")

def adminpage(request):
    return render(request,"mainpage/adminpage.html")

def catpage(request):
    return render(request,"mainpage/catpage.html")

def dev(request):
    return render(request,"mainpage/dev.html")

def editprofile(request):
    return render(request,"mainpage/edit-profile.html")

def profile(request):
    return render(request,"mainpage/profile.html")

def signin(request):
    return render(request,"mainpage/Sign_In.html")

def signup(request):
    return render(request,"mainpage/Sign_Up.html")

def landingpage(request):
    return render(request,"mainpage/landing_page.html")