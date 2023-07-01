from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','date_added','status','price',)
from .models import Category,Supplier

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone_number')
