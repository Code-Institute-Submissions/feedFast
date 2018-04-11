from django.test import TestCase
from django.urls import resolve
from .views import restaurant_detail, get_customer_view_restaurant
from .models import Restaurant
from accounts.models import Vendor

# Create your tests here.
class TestRestaurantDetail(TestCase):
    def test_restaurant_no_exist_return_404(self):
        response = self.client.get("restaurants/1/")
        self.assertEqual(response.status_code, 404)
        
    # def test_restaurant_exist_return_200(self):
    #     restaurant = Restaurant()
    #     vendor = Vendor()
    #     restaurant.save()
    #     response = self.client.get("restaurants/1/")
    #     self.assertEqual(response.status_code, 200)

   
class TestCustomerRestaurant(TestCase):
    def test_customerrestaurant_no_exist_return_404(self):
        response = self.client.get("restaurants/1/customerrestaurant")
        self.assertEqual(response.status_code, 404)
        
class TestCustomerRestaurantMenu(TestCase):
    def test_customerrestaurantmenu_no_exist_return_404(self):
        response = self.client.get("restaurants/3/menu/21/customermenu")
        self.assertEqual(response.status_code, 404)