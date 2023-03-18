from django.urls import path , include
from core_app.views import index

urlpatterns = [
    path('', index , name = 'home')
    
]