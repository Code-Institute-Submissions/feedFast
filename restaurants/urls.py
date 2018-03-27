from django.conf.urls import url
from .views import *

from .views import *

urlpatterns = [
    url(r'^$', get_restaurant_page, name='restaurants'), 
    url(r'^(\d+)', restaurant_detail, name='restaurant_detail'),
    url(r'^restaurant/create', create_restaurant, name='create_restaurant' ),
    url(r'^restaurants/(\d+)/addmenu', add_menu, name='add_menu' ),
]