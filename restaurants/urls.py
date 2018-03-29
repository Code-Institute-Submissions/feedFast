from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', get_restaurant_page, name='restaurants'), 
    url(r'^(\d+)/$', restaurant_detail, name='restaurant_detail'),
    url(r'^create', create_restaurant, name='create_restaurant' ),
    url(r'^(\d+)/addmenu', add_menu, name='add_menu' ),
    url(r'^(\d+)/menu/(\d+)/$', get_restaurant_menu, name='get_restaurant_menu'),
    url(r'^(\d+)/menu/(\d+)/edititem/(\d+)/$', edit_menu_item, name='edit_menu_item'),

 ]