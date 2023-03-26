from django.urls import path , include
from vendor_reg.views import *


urlpatterns = [
    path('', tester , name='vendor_reg'),
]