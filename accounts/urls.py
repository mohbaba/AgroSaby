from django.urls import path , include
from accounts.views import *


urlpatterns = [
    path('', account , name='registration'),
    path('buyer_reg.html', account, name='buyer_registration'),
    path('sign_in', sign_in, name= 'sign_in')
]