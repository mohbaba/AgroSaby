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

def account_page(request):
    return render(request , 'my-account.html')

def cart(request):
    return render(request , 'cart.html')

def checkout_page(request):
    return render(request , 'checkout.html')

def wishlist(request):
    return render (request , 'wishlist.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def sign_up(request):
    return render(request , 'signup.html')