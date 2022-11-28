from django.urls import path
from . import views


urlpatterns = [
    path('', views.input_data_about_user),
]
