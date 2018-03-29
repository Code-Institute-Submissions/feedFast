from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.http import HttpResponse
from .models import Restaurant, Menu, Menu_item
from .forms import RestaurantForm
from django.http import HttpResponseForbidden
from .forms import createMenuForm
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
            restaurant.vendor.user = request.user
            restaurant.save()
            return redirect('profile_vendor')
    else:
        form = RestaurantForm()
    
    return render(request, 'restaurant_reg.html', {'restaurantForm': form})

def get_restaurant_menu(request, restaurant_id, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menu_items = Menu_item.objects.all()
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant_menu_page.html', {'menu_items': menu_items, 'menu': menu, 'restaurant': restaurant})


# def edit_menu_item(request, restaurant_id, menu_id): 
#     item = get_object_or_404(Menu_item, pk=restaurant_id)

#     if request.method == "POST":
#         form = EditMenuItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect("restaurant_detail")
   
#     form = EditMenuItemForm(instance=item)
#     return render(request, "edit_menu_item.html", {'form': form})