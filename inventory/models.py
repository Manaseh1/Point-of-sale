from django.db import models

# Create your models here.
class Product(models.Model):
    class statuses(models.TextChoices):
        pending  ='pending','pending'
        decline = 'decline','decline'
        complete = 'complete','complete'
        approved = 'approved','approved'
        bulk = 'bulk','bulk'
    supplier = models.CharField(max_length=100,default = None)
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='product_images/',blank =True,null =True)
    category = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices = statuses.choices,default = statuses.pending)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name    