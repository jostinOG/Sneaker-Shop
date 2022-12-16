from django.shortcuts import render


# Create your views here.
# home page view -> This is the home page for the user
def home(request):
    return render(request, 'sneakers_online_store/home.html')


# admin page view
def admin(request):
    return render(request, 'sneakers_online_store/admin.html')


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin' and password == 'admin':
        return render(request, 'sneakers_online_store/admin.html')
    else:
        return render(request, 'sneakers_online_store/login.html')


# about page view-> This is the page where the user will know about you and your company
def about(request):
    return render(request, 'sneakers_online_store/about.html')


# contact page view -> This is the contact page for the user
def contact(request):
    return render(request, 'sneakers_online_store/contact.html')


# products page view -> This is the products page for the admin
def products(request):
    return render(request, 'sneakers_online_store/products.html')


# product page view -> This is the product page for the user
def product(request):
    return render(request, 'sneakers_online_store/product.html')


# cart page view -> This is the cart page for the user
def cart(request):
    return render(request, 'sneakers_online_store/cart.html')


# checkout page view -> Payment page for the user
def checkout(request):
    return render(request, 'sneakers_online_store/checkout.html')


# base page view-> This is the base page for all the pages
def base(request):
    return render(request, 'sneakers_online_store/base.html')
