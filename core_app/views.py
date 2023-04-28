from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
# Create your views here.

login_required(login_url='sign_in')
def index(request):
    
    
    try:
        user = request.user.id
        account = Accounts.objects.get(user=user)
        tru = account.get_user_type_display()
        print (tru)
        if account.get_user_type_display() == 'Seller':
            # perform action for seller
            is_seller = True
            print('works!!!')
            context = {
        'is_seller': is_seller,
    }
        else:
            # perform action for buyer
            is_seller = False
            print('not works!!!')
            context = {
        'is_seller': is_seller,
    }
        
    except Accounts.DoesNotExist:
        # handle case where account doesn't exist for user
        
        return render(request, 'index.html')
    
    
    return render(request, 'index.html',context)

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