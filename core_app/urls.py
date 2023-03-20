from django.urls import path , include
from core_app.views import *

urlpatterns = [
    path('', index , name = 'home'),
    path('about', about_us , name = 'about'),
    path('gallery',gallery_page, name = 'gallery'),
    path('contact_us', contact_page , name= 'contact'),
    path('shop', shop_page, name= 'shop'),
    
    
]