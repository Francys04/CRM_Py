from django.contrib import admin
# import admin profile from models
from .models import Userprofile

# Register your models here, as admin

admin.site.register(Userprofile)
