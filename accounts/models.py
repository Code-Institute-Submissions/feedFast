from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Vendor")
    
    def __str__(self):
        return self.user.username + " Vendor Account"
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Customer")
    city = models.CharField(max_length=100)
    #store all user data here. 
        
    def __str__(self):
        return self.user.username + " Customer Account"
    