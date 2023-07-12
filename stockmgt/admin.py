from django.contrib import admin
from .models import Stock

@admin.register(Stock)    
class StockAdmin(admin.ModelAdmin):
    list_display=('product','initial_quantity','intended_revenue','remaining_quantity')