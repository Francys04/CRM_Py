"""The path function is a fundamental part of Django's URL routing system, 
and it allows to map URLs to view functions or class-based views in your Django app."""
from django.urls import path

from . import views

"""for example => path('', views.clients_list, name='clients_list'):
This URL pattern matches the root URL of your application ('').
It maps to the clients_list view function.
The name parameter provides a name for this URL pattern, which can be used to reverse the URL in templates(html files) or views."""
urlpatterns = [
    path('', views.clients_list, name='clients_list'),
    path('<int:pk>/', views.clients_detail, name='clients_detail'),
    path('<int:pk>/delete/', views.clients_delete, name='clients_delete' ),
    path('<int:pk>/edit/', views.clients_edit, name='clients_edit' ),
    path('add/', views.clients_add, name='clients_add'),
]
