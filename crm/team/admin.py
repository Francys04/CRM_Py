from django.contrib import admin

# Register your models here.
# fpr admin pannel
from .models import Team, Plan

admin.site.register(Team)

admin.site.register(Plan)
