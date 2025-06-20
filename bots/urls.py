# bots/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.block_list, name='block_list'),
    path('save/', views.save_diagram, name='save_diagram'),
    path('export_json/', views.export_json, name='export_json'),

]
