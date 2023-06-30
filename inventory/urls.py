from django.urls import path
from inventory import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


appname = 'inventory'

urlpatterns = [
    path('Inventory_Dasboard/', views.inventory_dashboard, name='inventory_dashboard'),
]