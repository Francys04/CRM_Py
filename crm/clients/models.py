"""The models module is a core component of Django's Object-Relational Mapping (ORM) system, 
and it provides classes and fields for defining database tables and their relationships."""
from django.db import models
"""The User model is a part of Django's authentication system, and it provides a standard implementation 
for user authentication and user-related functionalities."""
from django.contrib.auth.models import User

from team.models import Team

""" Client class contains relationships, and methods to define the behavior and structure of the corresponding database table."""
class Client(models.Model):
    team= models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    create_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) #automatically updated
    
    # order alphabeticaly
    class Meta:
        ordering = ('name',)
    
    # func for represent the name of the new lead on db
    def __str__(self):
        return self.name
