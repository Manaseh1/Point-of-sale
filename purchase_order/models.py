from django.db import models
from inventory.models import Product,Supplier
# Create your models here.


class Order(models.Model):
    order_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.order_name
class Purchase(models.Model):
    order = models.ForeignKey(Order,on_delete= models.CASCADE,default =None,null = True)
    # order = models.CharField(max_length = 100)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, blank=True,default=None)
    email = models.EmailField(default= None)
    product_name = models.CharField(max_length=100,default=None)
    quantity = models.FloatField(default= 0)
    unit_price = models.FloatField(default=0)
    totals = models.FloatField(default= None,null=True)
    def get_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.product_name

