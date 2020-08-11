from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('contact-us/', views.contact_page, name='contact_page'),
    path('about-us/', views.about_page, name='about_page'),
]