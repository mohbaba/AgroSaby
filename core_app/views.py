from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from accounts.models import *
from vendor_reg.models import Product
# Create your views here.


def user_type_checker(request):
    try:
        user = request.user.id
        account = Accounts.objects.get(user=user)
        tru = account.get_user_type_display()
        if account.get_user_type_display() == 'Seller':
            # perform action for seller
            is_seller = True
            
    
        else:
            # perform action for buyer
            is_seller = False
            
        return is_seller

        
    except Accounts.DoesNotExist:
        # handle case where account doesn't exist for user
        
        return render(request, 'index.html')


login_required(login_url='sign_in')
def index(request):
    
    context = {
        'is_seller': user_type_checker(request),
    }
    
    return render(request, 'index.html',context)

@login_required(login_url='sign_in')
def shop_page(request):
    products = Product.objects.all()
    context = {
        'is_seller': user_type_checker(request),
        'products':products
    }
    return render(request, 'shop.html',context)

def about_us(request):
    
    return render(request , 'about.html')


def gallery_page(request, product_id):
     # Retrieve the product based on the product_id or handle errors if it doesn't exist
    product = get_object_or_404(Product, id=product_id)

    # Render the gallery template with the product details
    return render(request, 'gallery.html', {'product': product})
    

def contact_page(request):
    return render(request, 'contact-us.html')


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