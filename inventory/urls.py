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
    path('product_add', views.CreateProduct.as_view(), name='create_product'),
    path('product/list/', views.product_list, name='product_list'),

    path('category/delete/<int:category_id>/', views.delete_category, name='category_delete'),
    path('supplier/delete/<int:supplier_id>/', views.delete_supplier, name='supplier_delete'),
    path('product_edit/<pk>/', views.EditProduct.as_view(), name='product_edit'),
    path('product/delete/<int:product_id>/', views.delete_product, name='product_delete'),
]