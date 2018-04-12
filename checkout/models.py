from django.db import models
import datetime
from restaurants.models import Restaurant, Menu, Menu_item
from accounts.models import Customer
from django import forms
from django.forms import extras

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders')
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address_1 = models.CharField(max_length=40, blank=False)
    street_address_2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)
    reservation_date =  models.DateField (blank=False)
    reservation_time =  models.TimeField (blank=False)
    reservation_guests = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    item = models.ForeignKey(Menu_item, null=False)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.item.name, self.item.price)
