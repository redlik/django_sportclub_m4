from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    # paths for list and single post urls

    path('', views.view_basket, name='view_basket'),
]