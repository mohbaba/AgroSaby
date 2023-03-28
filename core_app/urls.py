from django.urls import path , include
from core_app.views import *

urlpatterns = [
    path('', index , name = 'home'),
    # path('about', about_us , name = 'about'),
    path('gallery',gallery_page, name = 'gallery'),
    path('contact', contact_page , name= 'contact'),
    path('shop', shop_page, name= 'shop'),
    path('account', account_page, name = 'account'),
    path('cart',cart , name='cart'),
    path('checkout', checkout_page , name = 'checkout'),
    path('wishlist', wishlist , name= ' wishlist'),
    path('shop_detail', shop_detail , name= ' shop_detail'),
    path('sign_up', sign_up, name = 'sign_up')
    
    
    
]