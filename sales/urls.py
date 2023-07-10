from django.urls import path
from sales import views
from .views import *



appname = 'sales'

urlpatterns = [
    
    path('sales_dashboard/', views.sales_dashboard, name='sales_dashboard'),
    path('POS/', views.pos, name='sales_pos'),

    path('receipt/<int:sale_id>/', views.receipt_view, name='receipt'),
    path('sales/delete/<int:sale_id>/', views.delete_sale, name='delete_sale'),
]