from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
