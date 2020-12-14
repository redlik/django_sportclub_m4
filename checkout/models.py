import uuid

from django.db import models
from django.db.models import Sum


from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=32, null=False, blank=False)
    address2 = models.CharField(max_length=32, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=6, null=False, blank=False)
    delivery_cost = models.DecimalField(max_digits=6, null=False, blank=False)
    grand_total = models.DecimalField(max_digits=12, null=False, blank=False)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitem')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitemtotal = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
