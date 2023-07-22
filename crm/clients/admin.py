""" The admin module is a built-in Django module that provides a powerful and 
customizable administration interface for managing your application's data."""
from django.contrib import admin

from .models import Client

"""admin.site.register(Client) tells Django to create a default admin interface for the Client model.
This interface allows to perform various administrative tasks on the Client model, such as CRUD."""
admin.site.register(Client)