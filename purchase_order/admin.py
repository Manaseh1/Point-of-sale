from django.contrib import admin
from .models import Purchase,Order
# Register your models here.
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('supplier','product_name','email','quantity','unit_price','totals',)

admin.site.register([Order])