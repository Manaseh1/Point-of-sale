from django.db import models
from inventory.models import Product

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    initial_quantity = models.PositiveIntegerField(default=0)
    remaining_quantity = models.PositiveIntegerField(default=0)
    unit_price = models.FloatField(default=0, blank=True, null=True)
    current_revenue  = models.FloatField(default=0, blank=True, null=True)
    intended_revenue = models.FloatField(default=0, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.product.quantity}"
