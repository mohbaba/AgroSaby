from django.shortcuts import render

# Create your views here.
def products(request):
    return render(request, 'shop.html')