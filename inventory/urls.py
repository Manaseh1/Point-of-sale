from django.urls import path
from inventory import views
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


appname = 'inventory'

urlpatterns = [
    path('Inventory_Dasboard/', views.inventory_dashboard, name='inventory_dashboard'),
    path('supplier/create/', views.create_supplier, name='create_supplier'),
    path('category/create/', views.create_category, name='create_category'),
    path('supplier/list/', views.supplier_list, name='supplier_list'),
    path('category/list/', views.category_list, name='category_list'),


    path('category/delete/<int:category_id>/', views.delete_category, name='category_delete'),
    path('supplier/delete/<int:supplier_id>/', views.delete_supplier, name='supplier_delete'),
]