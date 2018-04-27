# FeedFast
Ecommerce Web Application with User Authentication and Stripe Payments. FeedFast is a two-sided marketplace built for Restauranteurs and their customers. 
Built with busy schedules in mind this app has been designed to give users as much self-serve functionality as possible.  
This web app was built as a final project for the Code Institute's classroom bootcamp. It is a fictional Ecommerce site built with Python's Django framework - no template was used.

# Live Demo
Follow this link to view deployed version of the web app https://wolfenchic-feed-fast.herokuapp.com/

# Built with
- Django framework
- Python
- HTML
- CSS
- Bootstrap
- SQLite database
- AWS S3
- Javascript 
- jQuery 

# Views
Views called via URLs are Python functions that perform the different actions required to make the website function e.g. render a template, log someone in, log them out etc.

# Functionality Overview
This app has two primary user groups: Vendors and Customers.

Vendors have the ability to register their restaurants, create menus for those restaurants and add menu items to those menus. They also have the ability to add, edit and delete items from each of their menus. 

Customers have the ability to make a reservation in a restaurant and then proceed to purchase menu items. 

At present the table reservation functionality is simplistic. I intend to sophisticate this system over time and create a far more advanced booking feature. 

# Home
The Home App renders the base.html template, which contains a full webpage with navbar, content and footer. 

# Profiles & Accounts
User authentication has been created for both Vendors and Customers and both groups have distinct profile pages containing contextual data unique to that user, for e.g. their reservation data and their menus. 

The vendor profile page currently contains some hard coded elements within the following section: 
```<div class="vendorProfileStats">```
This is due to a lack of data however I wanted to present the concept of this page being a central analytics hub for subscribed vendors. 

The customer profile page contains a comprehensive How-To guide along with any reservation data belonging to the logged in customer. 

# Search
Search is built into the Restaurants App and uses a simple Python function to search through all the restaurant tags, giving the customer the ability to search for restaurants with specific types of food, for e.g. Mexican. 
```
def search_restaurants(request):
    match = request.GET.get('match')
    restaurants = Restaurant.objects.filter(tag__icontains=request.GET['query'])
    return render(request, "restaurant_page.html", {"restaurants": restaurants})
```
The results are filtered on the same page: restaurant_page.html
    
# Restaurants
The Restaurants app contains views for both customers and vendors. This app contains the restaurants, menus and menu items that have been added to the admin panel. 

# Payments/Cart
The Cart App stores the menu item, quantity and price of all menu items selected by the user and displays a basket total. The users table reservation request is also rendered on this page. The Checkout App then renders a form for a one-off Stripe payment. When payment is successful all Order data is then added to the Order table in the database. 

# Deployment / Hosting
This Project was deployed and is hosted on Heroku with automatic deploys from GitHub

# Databases / Static Files
When running locally, SQLite database was used & static and media files were stored locally. When deploying, Heroku Postgres was used as the server database & an Amazon S3 bucket was set up to host all the static files. settings.py file was amended for the database & static files to point to the online resources.  

# Testing
Automatic testing was carried out throughout the development of the project and progress can be viewed in the htmlcov folder. In addition I used <https://jigsaw.w3.org/css-validator/> to test CSS, <http://jshint.com/> to test Javascript files and responsiveness on <http://testsize.com/>. 

# Installation 