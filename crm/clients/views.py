"""The render function is used to render Django templates with context data. 
The get_object_or_404 function is used to retrieve an object from the database based on a specific model and primary key (pk).
The redirect function is used to redirect the user to a different URL."""
from django.shortcuts import render, get_object_or_404, redirect
"""login_required is a useful tool for restricting access to certain views 
in web application to only authenticated users. """
from django.contrib.auth.decorators import login_required
"""messages framework provides a simple way to send messages from the server to the user's web browser. """
from django.contrib import messages

from .models import Client
from .forms import AddClientForm

from team.models import Team

"""
The clients_list function uses the login_required decorator to ensure 
that only authenticated users can access the view. It retrieves a list of clients 
associated with the currently logged-in user and renders the data in the 'clients/clients_list.html' template."""
@login_required
def clients_list(request):
    clients = Client.objects.filter(create_by=request.user)
    
    return render(request, 'clients/clients_list.html', {
        'clients': clients
    }) 
    
"""It retrieves the details of a specific client associated with the currently logged-in user based on the provided primary key (pk). 
If the client does not exist, it raises a 404 error using get_object_or_404."""
@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, create_by=request.user, pk=pk)
    
    return render(request, 'clients/clients_detail.html', {
        'client': client
    }) 

"""Add new clients"""
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
    
"""Edit clients"""
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

    
    
"""Delete clients"""
def clients_delete(request, pk):
    client = get_object_or_404(Client,create_by=request.user, pk=pk)
    client.delete()
       
#  message for delte lead
    messages.success(request, 'The client was deleted !')
    return redirect('clients_list')
    
    