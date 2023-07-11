from django.contrib import admin
from .models import Sales, salesItems

@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['code', 'sub_total', 'grand_total', 'tax_amount', 'tax', 'tendered_amount', 'amount_change', 'date_added', 'date_updated']
    list_filter = ['date_added', 'date_updated']
    search_fields = ['code']

@admin.register(salesItems)
class SalesItemsAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'qty', 'total', 'sale']
    list_filter = ['sale']
    search_fields = ['product', 'sale__code']  # You can search by product name or sale code
