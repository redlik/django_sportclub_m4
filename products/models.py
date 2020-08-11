from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=120)
    friendly_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to='images/products/', blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
