from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponse
from .models import Restaurant, Menu, Menu_item
from .forms import RestaurantForm
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import createMenuForm
from .forms import EditMenuItemForm, createMenuItemsForm, ReservationForm
import datetime
# Create your views here.

def get_restaurant_page(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_page.html', {'restaurants': restaurants})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    form = createMenuForm()
    menus = Menu.objects.all()
    menu_item = Menu_item.objects.all()
    
    return render(request, "restaurant_detail.html", {'restaurant': restaurant, 'menus': menus, 'menu_items': menu_item, 'form': form})

def add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == "POST":

        form = createMenuForm(request.POST)
        if form.is_valid():

            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            
            return redirect(reverse('restaurant_detail', args=(restaurant_id,)))
            
            
    
def create_restaurant(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
        
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.vendor = request.user.vendor
            restaurant.save()
            return redirect('profile_vendor')
    else:
        form = RestaurantForm()
    
    return render(request, 'restaurant_reg.html', {'restaurantForm': form})

def get_restaurant_menu(request, restaurant_id, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    form = createMenuItemsForm()
    return render(request, 'restaurant_menu_page.html', {'form': form, 'menu': menu, 'restaurant': restaurant})
    
def get_customer_view_restaurant(request, id):
    restaurant = get_object_or_404(Restaurant, pk=id)
    menus = Menu.objects.all()
    form = ReservationForm()
    return render(request, 'customer_view_restaurant.html', {'form': form,'restaurant': restaurant, 'menus': menus})

def get_customer_menu(request, restaurant_id, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'customer_view_menu.html', {'menu': menu, 'restaurant': restaurant})


def edit_menu_item(request, restaurant_id, menu_id, menu_item_id): 
    menu = get_object_or_404(Menu, pk=menu_id)
    menu_item = get_object_or_404(Menu_item, pk=menu_item_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        form = EditMenuItemForm(request.POST, instance=menu_item)
        if form.is_valid():
            form.save()
            
            return redirect(reverse ('get_restaurant_menu', args=(restaurant_id, menu_id)))
   
    form = EditMenuItemForm(instance=menu_item)
    return render(request, "edit_menu_item.html", {'form': form, 'menu_item': menu_item, 'menu': menu, 'restaurant': restaurant})
    
def add_menu_item(request, restaurant_id, menu_id): 
    menu = get_object_or_404(Menu, pk=menu_id)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    form = createMenuItemsForm(request.POST)
    if form.is_valid():
        menu_item = form.save(commit=False)
        menu_item.menu  = menu
        menu_item.save()

            
    return redirect(reverse ('get_restaurant_menu', args=(restaurant_id, menu_id)))


def delete_menu_item(request,  restaurant_id, menu_id, menu_item_id):
    menu_item = get_object_or_404(Menu_item, pk=menu_item_id)
    menu_item.delete()
    return redirect(reverse ('get_restaurant_menu', args=(restaurant_id, menu_id)))

def search_restaurants(request):
    match = request.GET.get('match')
    restaurants = Restaurant.objects.filter(name__icontains=request.GET['query'])
    return render(request, "restaurant_page.html", {"restaurants": restaurants})

def book_table(request, restaurant_id): 
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            order = form.save(commit = False)
            print (order.reservation_guests, order.reservation_date, order.reservation_time)
            
            request.session['guests'] = order.reservation_guests
            request.session['reservation_date'] = order.reservation_date
            request.session['reservation_time'] = order.reservation_time
            
    return redirect(reverse ('get_customer_view_restaurant', args=(restaurant_id,)))
    
 