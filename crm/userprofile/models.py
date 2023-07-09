from django.db import models
# import user for this class
from django.contrib.auth.models import User


# Create your models here.

# create a db model for user
class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)