from django import forms
from .models import Restaurant, Menu, Menu_item 
from checkout.models import Order
from django.forms import extras
import re
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import Widget, Select, MultiWidget
from django.utils.safestring import mark_safe


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'city', 'image', 'tag')
        
class createMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name',)

class createMenuItemsForm(forms.ModelForm):
    class Meta:
        model = Menu_item
        fields = ('menu_category', 'name', 'description', 'price')

class EditMenuItemForm(forms.ModelForm):
    class Meta:
        model = Menu_item
        fields = ('menu', 'menu_category', 'name', 'description', 'price')

class ReservationForm(forms.ModelForm, forms.DateTimeField):
    class Meta: 
        model = Order
        fields = ('reservation_date', 'reservation_time', 'reservation_guests')
        widgets = {'reservation_date': extras.SelectDateWidget}
        
        

        
       
       
