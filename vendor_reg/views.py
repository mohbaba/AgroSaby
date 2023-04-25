from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from vendor_reg.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.



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
