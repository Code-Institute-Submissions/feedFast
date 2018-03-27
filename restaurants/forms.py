from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('vendor', 'name', 'description', 'city', 'image', 'tag')