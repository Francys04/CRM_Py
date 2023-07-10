from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Client
from .forms import AddClientForm

from team.models import Team

# Create your views here.
@login_required
def clients_list(request):
    clients = Client.objects.filter(create_by=request.user)
    
    return render(request, 'clients/clients_list.html', {
        'clients': clients
    }) 
    
    
@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, create_by=request.user, pk=pk)
    
    return render(request, 'clients/clients_detail.html', {
        'client': client
    }) 

# add new clients
@login_required
def clients_add(request):
    # show limit of number of user
    team = Team.objects.filter(created_by=request.user)[0]
    # /if request method is POST
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        # if data is valid
        if form.is_valid():
            team = Team.objects.filter(created_by = request.user)[0]
            
            client = form.save(commit=False)
            client.create_by = request.user
            client.team = team
            client.save()
            
            # message that list was added
            messages.success(request, 'This client was created')
            
            # add user to dashboard
            return redirect('clients_list')
        # if is not post request will be ampty form
    else:
        form = AddClientForm()
    
    return render(request, 'clients/clients_add.html', {
        'form': form,
        'team': team
    })
    
# edit
@login_required
def clients_edit(request, pk):
    lead = get_object_or_404(Client,create_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = AddClientForm(request.POST, instance=lead)
         
        if form.is_valid(): 
            form.save()
            
            messages.success(request, 'The changes of client was saved.')
            
            return redirect('clients_list')
    else:
        form = AddClientForm(instance=lead)
            
    return render(request, 'clients/clients_edit.html', {
        'form': form
    })

    
    
# delete
def clients_delete(request, pk):
    client = get_object_or_404(Client,create_by=request.user, pk=pk)
    client.delete()
       
#  message for delte lead
    messages.success(request, 'The client was deleted !')
    return redirect('clients_list')
    
    