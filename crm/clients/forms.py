"""The forms module is part of Django's django package and provides various form-related classes and 
utilities that simplify form creation, validation, and processing in your web applications."""
from django import forms

from .models import Client

"""The AddClientForm class provid by a Django ModelForm subclass. It allows to create a form for the Client model, 
which will automatically handle form rendering, validation, and saving data back to the model."""
class AddClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ("name", 'email', 'description')

        