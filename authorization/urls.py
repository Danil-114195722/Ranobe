from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('authorization', views.input_data_about_user),
]
