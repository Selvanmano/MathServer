from django.contrib import admin
from django.urls import path
from sgapp import views

urlpatterns = [
    path('', views. cumchurn_area, name='cumchurn_area'),
]