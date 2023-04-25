from django.db import models
from accounts.models import *
from django.contrib.auth import get_user_model
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'images',default = 'BlankPic.jpg' )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    