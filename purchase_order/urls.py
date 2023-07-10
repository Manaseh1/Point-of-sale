from django.urls import path
from .views import purchase_order

app_name = 'purchase_order'
urlpatterns = [
    path('',purchase_order,name='purchase_order'),
]