from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # paths for list and single post urls

    path('shop/', views.all_products, name='all_products'),
    path('shop/product/<product_id>/', views.product_detail, name='product_detail')
]