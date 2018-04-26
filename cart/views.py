from django.shortcuts import render, redirect, get_object_or_404, reverse
from restaurants.models import Restaurant, Menu, Menu_item
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from checkout.models import Order, OrderLineItem

def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    
    booking = {'guests': request.session.get('guests', 0),
                    'reservation_date_day': request.session.get('reservation_date_day', 0),
                    'reservation_date_month': request.session.get('reservation_date_month', 0),
                    'reservation_date_year': request.session.get('reservation_date_year', 0),
                    'reservation_time': request.session.get('reservation_time', 0)
        }
   
    context.update(booking)
    return render(request, "cart/view_cart.html", context)
    
@login_required()
def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart
    
    menu_item = get_object_or_404(Menu_item, pk=id)
    order = get_object_or_404(Order, pk=id)
    menu = menu_item.menu
    restaurant = menu.restaurant
    # order = customer.order.restaurant
   
    return redirect(reverse('get_customer_menu', args=(restaurant.id, menu.id)))
    
    

def delete_cart_item(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')    