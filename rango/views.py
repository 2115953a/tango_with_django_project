from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
                    'about_url': reverse('rango:about')}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by me!',
                    'index_url': reverse('rango:index')}
    return render(request, 'rango/about.html', context=context_dict)