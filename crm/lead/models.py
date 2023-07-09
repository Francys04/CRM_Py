from django.db import models
from django.contrib.auth.models import User
from team.models import Team


class Lead(models.Model):
    # what is priority is this
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    
    CHOISE_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'
    
    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )
    
    team= models.ForeignKey(Team, related_name='leads', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=250)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    
    priority = models.CharField(max_length=20, choices=CHOISE_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=NEW)
    converted_to_client = models.BooleanField(default=False)
    create_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) #automatically updated
    
    # order list alphabetical
    class Meta:
        ordering = ('name',)
    
    # func for represent the name of the new lead on db
    def __str__(self):
        return self.name
