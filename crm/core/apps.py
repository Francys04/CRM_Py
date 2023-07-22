"""AppConfig class is a configuration class that provides metadata and settings for a particular app."""
from django.apps import AppConfig

"""default_auto_field -> This attribute specifies the default primary key field to use for models defined in the app. 
In this case, it is set to 'django.db.models.BigAutoField'"""
class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    """name:It is set to 'core', which should match the name of the app's directory and 
    the value used in the INSTALLED_APPS setting in your project's settings file."""
    name = 'core'
