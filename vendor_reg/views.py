from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def tester(request):
    return render(request, 'shop.html')