# add messages
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead
from clients.models import Client
from team.models import Team

# Create your views here.

# represent on dashboard data of lead created
@login_required
def leads_list(request):
    leads = Lead.objects.filter(create_by=request.user, converted_to_client=False)
    
    return render(request, 'lead/leads_list.html', {
        'leads': leads
    })

# detail of lead
@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead,create_by=request.user, pk=pk)
   
    
    return render(request, 'lead/leads_detail.html', {
        'lead': lead
    })

# delete leads
def leads_delete(request, pk):
    lead = get_object_or_404(Lead,create_by=request.user, pk=pk)
    lead.delete()
       
#  message for delte lead
    messages.success(request, 'The lead was deleted !')
    return redirect('leads_list')

# edit lead
@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead,create_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
         
        if form.is_valid(): 
            form.save()
            
            messages.success(request, 'The changes of lead was saved.')
            
            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
            
    return render(request, 'lead/leads_edit.html', {
        'form': form
    })

# create for Add lead button
@login_required
def add_lead(request):
    # /if request method is POST
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        # if data is valid
        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.create_by = request.user
            lead.team=team
            lead.save()
            
            # message that list was added
            messages.success(request, 'This lead was created')
            
            # add user to dashboard
            return redirect('dashboard')
        # if is not post request will be ampty form
    else:
        form = AddLeadForm()
    
    return render(request, 'lead/add_lead.html', {
        'form': form
    })
    
# conver to client
@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead,create_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]
    
    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        create_by=request.user,
        team=team,
    )
    
    lead.converted_to_client = True
    lead.save()
    
    messages.success(request, 'This lead was converted to the client')
    
    return redirect('leads_list')