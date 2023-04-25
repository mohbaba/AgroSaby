from django.urls import path , include
from accounts.views import *



urlpatterns = [
    path('', account , name='registration'),
    path('register', account, name='buyer_registration'),
    path('sign_in', sign_in, name= 'sign_in'),
    path('logout', log_user_out, name= 'logout'),
    
]