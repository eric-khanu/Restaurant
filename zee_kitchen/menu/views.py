from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'menu/index.html')

def menus(request):
    return render(request, 'menu/menus.html')

def locations(request):
    return render(request, 'menu/locations.html')

def order(request):
    return render(request, 'menu/order.html')

def service(request):
    return render(request, 'menu/service.html')