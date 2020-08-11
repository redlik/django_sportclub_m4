from django.contrib import admin
from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    # paths for list and single post urls

    path('', views.posts_list, name='posts_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail_view'),
]