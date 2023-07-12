from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Product
from stockmgt.models import Stock

@receiver(post_save, sender=Product)
def create_stock(sender, instance, created, **kwargs):
    if created:
        unitprice = instance.price
        qty = instance.quantity
        
        expectedRevenue = unitprice * qty
        Stock.objects.create(product=instance,initial_quantity=qty,intended_revenue=expectedRevenue,unit_price=unitprice,remaining_quantity = qty)
