from time import timezone
from django.utils import timezone
from django.db import models
from inventory.models import Product
from decimal import Decimal

class Sales(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    sub_total = models.FloatField(default=0, blank=True, null=True)
    grand_total = models.FloatField(default=0, blank=True, null=True)
    tax_amount = models.FloatField(default=0, blank=True, null=True)
    tax = models.FloatField(default=0, blank=True, null=True)
    tendered_amount = models.FloatField(default=0, blank=True, null=True)
    amount_change = models.FloatField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now, blank=True, null=True) 
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True) 

    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale = models.ForeignKey(Sales,on_delete=models.CASCADE,related_name='sales_items')
    product = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(default=0, blank=True, null=True)
    qty = models.FloatField(default=0, blank=True, null=True)
    total = models.FloatField(default=0, blank=True, null=True)

class MoneyControl(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    Amount = models.FloatField(default=0, blank=True, null=True)
