from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    prepopulated_fields={'name': ('friendly_name',)}
    search_fields = ('name', 'friendly_name')
    ordering = ('friendly_name','name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields={'slug':('name',)}
    ordering = ('name',)

