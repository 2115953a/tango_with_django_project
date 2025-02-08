from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    about_url = reverse('about')
    return HttpResponse(f"Rango says hey there partner! <a href='{about_url}'>About</a>")

def about(request):
    index_url = reverse('index')
    return HttpResponse(f"Rango says here is the about page. <a href='{index_url}'>Index</a>")