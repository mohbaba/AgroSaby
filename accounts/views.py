from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from accounts.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def account(request):
    
    if request.method == 'POST':
        firstname = request.GET.get('firstname')
        username = request.GET.get('username')
        lastname = request.GET.get('lastname')
        email = request.GET.get('email')
        password1 = request.GET.get('passsword')
        password2 = request.GET.get('password2')
        phone_no = request.GET.get('phone')
        acc_type = request.GET.get('acc_type')
        
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('buyer_reg.html')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken try another one ')
            else:
                user = User.objects.create_user(email=email, password=password1)
                user.save()
                acc = Accounts(firstname = firstname, lastname = lastname, phone_number = phone_no, user_type = acc_type)
                acc.save()
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('buyer_reg.html')
        
        
        
    else:
        return render(request, 'buyer_reg.html')


def about_us(request):
    
    return render(request , 'about.html')