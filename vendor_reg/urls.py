from django.urls import path , include
from vendor_reg.views import *


urlpatterns = [
    path('',seller_dashboard,name = 'sell_admin'),
    path('product_add',add_product,name = 'product_add'),
    path('seller_products',seller_products, name='seller_products'),
    
    
]