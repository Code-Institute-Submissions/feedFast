from django.shortcuts import get_object_or_404
from restaurants.models import Restaurant, Menu, Menu_item
from decimal import Decimal


def get_cart_items_and_total(cart):

    cart_items = []
    total = 0
    for menu_item_id, item_quantity in cart.items():
        this_menu_item = get_object_or_404(Menu_item, pk=menu_item_id)
        this_menu = this_menu_item.menu
        this_restaurant = this_menu.restaurant
        this_total = this_menu_item.price * Decimal(item_quantity)
        total += this_total
        this_item = {
            'restaurant': this_restaurant,
            'menu': this_menu,
            'menu_item': this_menu_item, 
            'quantity': item_quantity,
            'total': this_total,
        }
        cart_items.append(this_item)

    return { 'cart_items': cart_items, 'total': total }
    

