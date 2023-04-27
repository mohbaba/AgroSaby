from django.urls import path , include
from vendor_reg.views import *


urlpatterns = [
    path('',seller_dashboard,name = 'sell_admin')
]