from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from .views import login

# Create your tests here.
class TestAccountsViews(TestCase):
    def test_GET_login_ok(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        
    def test_GET_login_resolves_to_login_form(self):
        found = resolve('/accounts/login/')  
        self.assertEqual(found.func, login) 
        
    def test_POST_can_log_in(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/", {'username': 'user', 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)
    
    def test_POST_can_redirect_after_login(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/?next=/accounts/profile/", {'username': 'user', 'password': 'password'})
        self.assertRedirects(response, "/accounts/profile/", status_code=302, target_status_code=404)
    
    def test_profile_requires_login(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/?next=/accounts/profile/vendor", {'username': 'user', 'password': 'password'})
        self.assertRedirects(response, "/accounts/profile/vendor", status_code=302, target_status_code=200)
    
    def test_profile_requires_login_customer(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/?next=/accounts/profile/customer", {'username': 'user', 'password': 'password'})
        self.assertRedirects(response, "/accounts/profile/customer", status_code=302, target_status_code=200)
        
    
    def test_can_logout(self):
        self.user = User.objects.create_user(username='user', password='password')
        response = self.client.post("/accounts/login/", {'username': 'user', 'password': 'password'})
        self.assertIn('_auth_user_id', self.client.session)
        response = self.client.get("/accounts/logout/")
        self.assertNotIn('_auth_user_id', self.client.session)
    
            
    def test_GET_register_vendor(self):
        response = self.client.get("/accounts/register/vendor/")
        self.assertEqual(response.status_code, 200)
        
    def test_GET_register_customer(self):
        response = self.client.get("/accounts/register/customer/")
        self.assertEqual(response.status_code, 200)
    
    def test_POST_register_vendor(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post("/accounts/register/vendor/", details)
        self.assertRedirects(response, "/accounts/profile/vendor", status_code=302, target_status_code=200)
    
    def test_POST_register_customer(self):
        details = {
            'username': 'user',
            'email': 'user@example.com',
            'password1': 'password',
            'password2': 'password',
            'city': 'city',
        }
        response = self.client.post("/accounts/register/customer/", details)
        self.assertRedirects(response, "/accounts/profile/customer", status_code=302, target_status_code=200)

