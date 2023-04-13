from django.urls import path , include
from accounts.views import *


urlpatterns = [
    path('', accounts , name='registration'),
]