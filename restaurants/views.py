from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Restaurant, Menu, Menu_item
from .forms import RestaurantForm
# Create your views here.

def get_restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_page.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    menu = Menu.objects.all()
    menu_item = Menu_item.objects.all()
    return render(request, "restaurant_detail.html", {'restaurant': restaurant, 'menu': menu, 'menu_items': menu_item})