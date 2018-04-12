from django.shortcuts import render, redirect, get_object_or_404
from restaurants.models import Restaurant
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def view_cart(request):
    cart = request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    
    booking = {'guests': request.session.get('guests', 0),
                    'reservation_date_day': request.session.get('reservation_date_day', timezone.now()),
                    'reservation_date_month': request.session.get('reservation_date_month', timezone.now()),
                    'reservation_date_year': request.session.get('reservation_date_year', timezone.now()),
                    'reservation_time': request.session.get('reservation_time', timezone.now())
        }
    context.update(booking)
        
    return render(request, "cart/view_cart.html", context)
 

def add_to_cart(request):
    id = request.POST['id']
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, 0) + quantity
    
    request.session['cart'] = cart
 
    return redirect('home')
    
    

def delete_cart_item(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart   
    return redirect('view_cart')    