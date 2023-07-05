from django.urls import path
from sales import views
from .views import *



appname = 'sales'

urlpatterns = [
    
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path('POS/', views.pos, name='sales_pos'),
    path('additem/<pk>', views.pos, name='add_pos'),

]