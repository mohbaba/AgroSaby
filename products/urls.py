from django.urls import path , include
from core_app.views import homePageView

urlpatterns = [
    path('', homePageView , name = 'products')
    
]