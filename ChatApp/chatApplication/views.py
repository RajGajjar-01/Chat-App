from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def landing(request):
    return render(request, 'chatApplication/landing.html')

def home(request):
    return render(request, 'chatApplication/home.html')