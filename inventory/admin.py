from django.contrib import admin
from .models import Category,Supplier,Product
# Register your models here.
@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','supplier','category','date_added','status','price',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number')