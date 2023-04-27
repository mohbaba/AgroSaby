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
