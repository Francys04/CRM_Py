from django.db import models
from django.contrib.auth.models import User

"""This class is for limitation of number of user"""
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    max_leads = models.IntegerField()
    max_clients = models.IntegerField()
    
    
    def __str__(self):
        return self.name

"""The Team class model allows you to store information about teams, their associated plan, 
their members, and the user who created the team, 
providing a foundation for managing team-related data in your Django application."""
class Team(models.Model):
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.CASCADE,  null=True)
    name = models.CharField(max_length=150)
    memebers = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
