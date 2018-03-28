from django.db import models
from django import forms
from accounts.models import Vendor
from .choices import MENU_CATEGORY_CHOICES


# Create your models here.
class Restaurant(models.Model):
    vendor = models.ForeignKey(Vendor, related_name="restaurants")
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    tag = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=64, default="Dublin")
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="menus")
    name = models.CharField(max_length=254, default="standard",blank=False)

  
    def __str__(self):
        return self.restaurant.name + " " + self.name
    
class Menu_item(models.Model):
    menu = models.ForeignKey(Menu, related_name='items')
    # restaurant = models.ForeignKey(Restaurant, related_name='restaurant')
    menu_category = models.IntegerField(choices=MENU_CATEGORY_CHOICES, default=1)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.IntegerField(default=0)
    

    def __str__(self):
        return self.menu.restaurant.name + " " +  self.menu.name + " " + self.name
