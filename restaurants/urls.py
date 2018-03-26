from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_restaurant_page, name='restaurants'), 
    url(r'^(\d+)', restaurant_detail, name='restaurant_detail'),
]