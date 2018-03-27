from django.conf.urls import url, include 
from .views import *
from . import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name='logout'),
    url(r'^login/', login, name='login'),
    url(r'^profile/vendor', profile_vendor, name='profile_vendor'),
    url(r'^profile/customer', profile_customer, name='profile_customer'),
    url(r'^register/vendor/', register_vendor, name='register_vendor'),
    url(r'^register/customer/', register_customer, name='register_customer'),
    url(r'^password-reset/', include(urls_reset)),
]