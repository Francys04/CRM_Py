"""This statement access the path function, which is a fundamental tool for defining URL patterns in your Django application."""
from django.urls import path

from . import views

"""This URL pattern maps the root URL of your application 
("empty") to the dashboard view function."""
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
