from django.contrib.auth.models import User
import django_filters
from models import Restaurant 

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'city', 'image', 'tag']
