from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from lead.models import Lead
from clients.models import Client
from team.models import Team

# create dashboard
@login_required
def dashboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-create_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-create_at')[0:5]
    return  render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
