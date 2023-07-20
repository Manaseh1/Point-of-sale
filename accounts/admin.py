from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'first_name', 'last_name')
    
@admin.register(NewEmployee)
class NewEmployeeAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'first_name', 'last_name','role')