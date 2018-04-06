from django.conf.urls import url, include
from .views import add_to_cart, view_cart, delete_cart_item

urlpatterns = [
    url(r'^add/$', add_to_cart, name='add_to_cart'), 
    url(r'^view/$', view_cart, name='view_cart'),
    url(r'^delete/(\d+)', delete_cart_item, name='delete_cart_item'),
    ]