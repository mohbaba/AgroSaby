from django.db import models
from accounts.models import *
from django.contrib.auth import get_user_model
from datetime import datetime
import uuid



# Create your models here.

class Product(models.Model):
    # id = models.UUIDField(primary_key = True, default= uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length= 50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
    # image = models.ImageField(upload_to='products')
    user = models.CharField(max_length = 100, default='oreoluwa')
    img = models.ImageField(upload_to = 'images',default = 'BlankPic.jpg' )
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
    
    def __str__(self):
        return self.user
    