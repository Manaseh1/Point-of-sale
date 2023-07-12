from django.urls import path
from .views import *

app_name = 'purchase_order'
urlpatterns = [
    path('',purchase_order,name='purchase_order'),
    path('save-form-data/', save_form_data, name='save_form_data'),
    path('PurchaseItems/', purchase_items, name='purchase_items'),
]