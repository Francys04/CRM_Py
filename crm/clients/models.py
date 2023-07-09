from django.db import models
from django.contrib.auth.models import User

from team.models import Team

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
