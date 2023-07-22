from django.contrib import messages
"""The get_object_or_404 function is used to retrieve an object from the database based on a specific model and primary key (pk). 
If the object does not exist, it raises a Http404 exception, resulting in a "Page Not Found" error page being displayed. """
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Team
from .forms import TeamForm

# Create your views here.

"""The view handles both the GET and POST requests to display the team edit form and process the form submission, respectively."""
@login_required
def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, 'The changes was saved!')
            return redirect('myaccount')
    else:
        form = TeamForm(instance=team)
        
    return render(request, 'team/edit_team.html', {
        'team': team,
        'form': form
    })

