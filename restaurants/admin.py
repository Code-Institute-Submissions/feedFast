from django.contrib import admin
from .models import Restaurant, Menu, Menu_item

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Menu_item)
