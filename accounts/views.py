from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def account(request):
    
    if request.method == 'POST':
        firstname = request['firstname']
        lastname = request['lastname']
        email = request['email']
        password1 = request['passsword']
        password2 = request['password2']
        phone_no = request['phone']
        acc_type = request['acc_type']
        
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('buyer_reg.html')
            else:
                user = User.objects.create_user(email=email, password=password1)
                acc = Accounts()
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('buyer_reg.html')
        
        
        
    else:
        return render(request, 'buyer_reg.html')


def about_us(request):
    
    return render(request , 'about.html')