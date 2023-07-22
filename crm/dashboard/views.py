from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from lead.models import Lead
from clients.models import Client
from team.models import Team

"""Decorator requires the user to be authenticated (logged in) to access it, thanks to the @login_required decorator. 
This view is responsible for rendering the content of the dashboard page for an authenticated user."""
@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-create_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-create_at')[0:5]
    return  render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
