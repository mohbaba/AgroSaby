from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from core_app.urls import *
from vendor_reg.urls import *
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
                # This creates the user acccounts and saves them to the database
                user = User.objects.create_user(username = username,email=email, password=password1,first_name = firstname, last_name = lastname)
                acc = Accounts(firstname = firstname, lastname = lastname, phone_number = phone_no, user_type = acc_type, user =user,email=email)
                acc.save()
                
                #log user in and direct to home page
                
                user_login = authenticate(username=username, password=password1)
                login(request,user_login)
                
                return redirect('home')
        else:
            messages.info(request, 'Passwords do not match!')
            return render(request, 'buyer_reg.html', context)
            # return redirect('buyer_reg.html',context)
        
        
        
    else:
        return render(request, 'buyer_reg.html', context)


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request , username= username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Success!')
            
            return redirect('/')
            # return redirect('/admin_/tester')
        
        else:
            messages.error(request, 'User not found! Create new account')
            return redirect('sign_in')
    else:
        return render(request , 'sign_in.html')
    
@login_required(login_url= 'sign_in')
def log_user_out(request):
    logout(request)
    return redirect('sign_in')


# @login_required(login_url = 'sign_in')
# def type_checker(request):
#     user = request.user
    
#     try:
#         account = Accounts.objects.get(user=user)
#         tru = account.get_user_type_display()
#         print (tru)
#         if account.get_user_type_display() == 'Seller':
#             # perform action for seller
#             is_seller = True
#             print('works!!!')
#         else:
#             # perform action for buyer
#             is_seller = False
#             print('not works!!!')
        
#     except Accounts.DoesNotExist:
#         # handle case where account doesn't exist for user
#         pass
    
#     context = {
#         'is_seller': is_seller,
#     }
#     return render(request, 'index.html',context)