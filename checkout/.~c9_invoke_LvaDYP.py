from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from restaurants.models import Restaurant, Menu, Menu_item
from decimal import Decimal
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.conf import settings
import stripe
from django.contrib import messages
from restaurants.forms import ReservationForm
import datetime 
from .utils import save_order_items, charge_card, send_confirmation_email
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template, render_to_string

stripe.api_key = settings.STRIPE_SECRET
# Create your views here.
def checkout(request):
    print("**** Enter checkout ***")
    print(request.method)
    if request.method=="POST":
        print("you are posting - great")
        # Save The Order
        order_form = OrderForm(request.POST)
        order = order_form.save(commit=False)
        y = int(request.session['reservation_date_year'])
        m = int(request.session['reservation_date_month'])
        d = int(request.session['reservation_date_day'])
        order.reservation_date = datetime.date(y,m,d)
        order.reservation_time = request.session['reservation_time']
        order.reservation_guests = request.session['guests']
        order.customer = request.user.customer
        order.save()
        
        # Save the Order Line Items
        cart = request.session.get('cart', {})
        for id, quantity in cart.items():
            menu_item = get_object_or_404(Menu_item, pk=id)
            order_line_item = OrderLineItem(
                order = order,
                item = menu_item,
                quantity = quantity
                )
            order_line_item.save()
            print("did cart stuff")
        
        # Charge the Card
        payment_form = MakePaymentForm(request.POST)
        print("In charge card section")
        if payment_form.is_valid():
            items_and_total = get_cart_items_and_total(cart)
            total = items_and_total['total']
            total_in_cent = int(total*100)
            
        try:
                customer = stripe.Charge.create(
                    amount=total_in_cent,
                    currency="EUR",
                    description="Dummy Transaction",
                    card=payment_form.cleaned_data['stripe_id'],
                )
        except stripe.error.CardError:
                messages.error(request, "Your card was declined!")  
        
        if customer.paid:
                messages.error(request, "You have successfully paid")
                # Send Email
                # context = {
                #     'site_name': "Blah Blah dot com",
                #     'user': request.user,
                # }
                # context.update(items_and_total)
                # message = render_to_string('checkout/text_confirmation_email.html', context)
                # html_message = render_to_string('checkout/html_confirmation_email.html', context)
                
                # subject = 'Thanks for buying our stuff!'
                # message = message
                # from_email = settings.SYSTEM_EMAIL
                # to_email = [request.user.email]
    
                # send_mail(subject,message,from_email,to_email,fail_silently=True,html_message=html_message)
                
                #Clear the Cart
                # del request.session['cart']
                return redirect("home")


    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE_KEY }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context)