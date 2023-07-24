from django.urls import path
from .views import *

appname = 'accommodation'

urlpatterns = [
    path('', home, name='home'),
    path('room_list/', room_list, name='room_list'),
    path('add_room/', add_room, name='add_room'),
    path('edit_room/<int:room_id>/', edit_room, name='edit_room'),
    path('delete_room/<int:room_id>/', delete_room, name='delete_room'),
    path('booking_list/', booking_list, name='booking_list'),
    path('add_booking/', add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', delete_booking, name='delete_booking'),
    path('customer_list/', customer_list, name='customer_list'),
    path('add_customer/', add_customer, name='add_customer'),
    path('edit_customer/<int:customer_id>/', edit_customer, name='edit_customer'),
    path('delete_customer/<int:customer_id>/', delete_customer, name='delete_customer'),
]
