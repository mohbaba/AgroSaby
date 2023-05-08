from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from vendor_reg.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.



@login_required(login_url='sign_in')
def seller_dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url='sign_in')
def add_product(request):
    if request.method == 'POST':
        user = request.user.username
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        image = request.FILES.get('image')
        
        # Adds the info to the product database
        product = Product(name=product_name, description=description, price=price, quantity = quantity, img = image, user = user)
        product.save()
        
        
        messages.success(request, 'Product Successfully Added!')
        
        return redirect('/seller_admin_')
    
    
    else:    
        return render(request, 'add_product.html')
    
    
@login_required(login_url='sign_in')
def seller_products(request):
    user = request.user
    products_list = Product.objects.filter(user = user)
    context = {'products': products_list}
    return render(request, 'seller_products.html',context)
    
    
