from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

User = get_user_model()
USER_CHOICE = (
        ("1","Buyer"),
        ("2","Seller")
    )
    
class Accounts(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    firstname = models.CharField(max_length= 30)
    lastname = models.CharField(max_length= 20)
    phone_number = PhoneNumberField(blank=True)
    user_type = models.CharField(
        max_length = 20,
        choices = USER_CHOICE,
        default = '1',
    )
    
    def __str__(self) :
        return self.user.username


