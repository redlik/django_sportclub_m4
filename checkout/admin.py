from django.contrib import admin
from .models import Order, OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'delivery_cost', 'order_total', 'grand_total',)

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'city', 'address1', 'address2', 'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name', 'ordet_total', 'delivery_cost', 'grand_total'),

    ordering = ('-date',)