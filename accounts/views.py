from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm
from .forms import UserRegistrationForm, CustomerRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Vendor, Customer
from restaurants.models import Restaurant

# Create your views here.
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("home")
    
def login(request):
    redirect_to = request.GET.get('next', 'home')
    
    if request.method=='POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            #Authenticate the user
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))
            
            # if the user is a user, and has correct password
            if user is not None:
                #Log them in
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(redirect_to)
    
            else:
                # say no
                form.add_error(None, "Your username or password was not recognised")
        
    else:
        form = UserLoginForm()
    
    
    return render(request, 'accounts/login.html', { 'form': form })


@login_required()
def profile_vendor(request):
    return render(request, 'accounts/profile_vendor.html')

@login_required()
def profile_customer(request):
    return render(request, 'accounts/profile_customer.html')
    
    
def register_vendor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            vendor = Vendor()
            vendor.user = user
            vendor.save

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        user_form = UserRegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})
    
def register_customer(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        type_form = CustomerRegistrationForm(request.POST)
        
        if user_form.is_valid() and type_form.is_valid():
            user = user_form.save()
            customer = type_form.save(commit=False)
            customer.user = user
            customer.save()
            

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")

    else:
        user_form = UserRegistrationForm()
        type_form = CustomerRegistrationForm()

    return render(request, 'accounts/register.html', {'user_form': user_form, 'type_form': type_form}) 

