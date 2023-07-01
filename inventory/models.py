from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    class statuses(models.TextChoices):
        pending  ='pending','pending'
        decline = 'decline','decline'
        complete = 'complete','complete'
        approved = 'approved','approved'
        bulk = 'bulk','bulk'
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    image = models.ImageField(upload_to='product_images/',blank =True,null =True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices = statuses.choices,default = statuses.pending)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name   