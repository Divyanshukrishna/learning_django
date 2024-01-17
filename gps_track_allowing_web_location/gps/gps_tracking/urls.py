from django.contrib import admin
from django.urls import path
from gps_tracking import views

urlpatterns = [
    path('',views.home, name="home"),
]