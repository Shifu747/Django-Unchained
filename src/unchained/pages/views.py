from urllib import request
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'home.html', {})