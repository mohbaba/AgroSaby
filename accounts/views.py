from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from core_app.urls import *
from accounts.models import *
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def account(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        username = request.POST.get('username')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone_no = request.POST.get('phone')
        acc_type = request.POST.get('acc_type')
        
        context = {
                    'email': email,
                    'username': username,
                    'firstname': firstname,
                    'lastname': lastname,
                    'phone': phone_no,
                    'acc_type': acc_type,
                }

        
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                # return redirect('buyer_reg.html', context)
                return render(request, 'buyer_reg.html', context)
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken try another one ')
                # return redirect('buyer_reg.html', context)
                return render(request, 'buyer_reg.html', context)
            else:
                user = User.objects.create_user(username = username,email=email, password=password1)
                acc = Accounts(firstname = firstname, lastname = lastname, phone_number = phone_no, user_type = acc_type, user =user)
                acc.save()
                
                #log user in and direct to home page
                
                # user_login = auth.authenticate(username=username, password=password1)
                # auth.login(request,user_login)
                return redirect('home')
        else:
            messages.info(request, 'Passwords do not match!')
            return render(request, 'buyer_reg.html', context)
            # return redirect('buyer_reg.html',context)
        
        
        
    else:
        return render(request, 'buyer_reg.html', context)


def about_us(request):
    
    return render(request , 'about.html')