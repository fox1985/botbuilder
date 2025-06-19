# bots/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.block_list, name='block_list'),
    path('export/', views.export_json, name='export_json'),
]
