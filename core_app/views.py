from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    return render(request ,'index.html')

def about_us(request):
    
    return render(request , 'about.html')


def gallery_page(request):
    return render (request, 'gallery.html')

def contact_page(request):
    return render(request, 'contact-us.html')

def shop_page(request):
    return render(request, 'shop.html')