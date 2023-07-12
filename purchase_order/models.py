from django.db import models
from inventory.models import Product,Supplier
# Create your models here.
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, blank=True,default=None)
    product_name = models.CharField(max_length=100,default=None)
    quantity = models.FloatField(default= 0)
    unit_price = models.FloatField(default=0)
    totals = models.FloatField(default= None,null=True)
    def get_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.product_name
class dummy(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, blank=True,default=None)
