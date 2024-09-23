from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menus/', views.menus, name='menus'),
    path('locations/', views.locations, name='locations'),
    path('order/', views.order, name='order'),
    path('service/', views.service, name='service'),
    
]