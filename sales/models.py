from time import timezone
from django.db import models
from inventory.models import Product
from decimal import Decimal

class Sales(models.Model):
    sale_id = models.CharField(max_length=10, unique=True, editable=False)
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateField(auto_now_add=True) 
    date_updated = models.DateTimeField(auto_now=True) 

    def save(self, *args, **kwargs):
            if not self.sale_id:
                # Generate a unique sale_id if it doesn't exist
                last_sale = Sales.objects.order_by('-sale_id').first()
                last_sale_number = int(last_sale.sale_id[2:]) if last_sale else 0
                self.sale_id = f"SL{last_sale_number + 1:04d}"
            super().save(*args, **kwargs)

    def __str__(self):
        return self.sale_id

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)
    total = models.FloatField(default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default= Decimal(0))
    

    def __str__(self):
        return self.sale_id.sale_id
