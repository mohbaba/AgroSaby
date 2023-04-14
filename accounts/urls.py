from django.urls import path , include
from accounts.views import *


urlpatterns = [
    path('', account , name='registration'),
]