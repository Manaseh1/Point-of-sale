from django.contrib import admin
from .models import Customer, Room, Booking

# Register the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number']

# Register the Room model
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'capacity', 'price_per_night', 'is_available', 'description']

# Register the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'room', 'check_in_date', 'check_out_date', 'is_paid']
