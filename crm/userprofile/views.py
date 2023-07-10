from django.shortcuts import render, redirect
# import pack with auth with pass, username, email
from django.contrib.auth.forms import UserCreationForm
# import userprofile for check information
from .models import Userprofile
# for my account
from django.contrib.auth.decorators import login_required
# for team account
from team.models import Team

# Create your views here.

def signup(request):
    # check if the form has been submited
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if info is correct
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            # invitations for users
            team = Team.objects.create(name='The team name', created_by=request.user)
            team.memebers.add(request.user)
            team.save()
            
            return redirect('/log_in')
        # if not post request
        else:
            form = UserCreationForm()
        
    form = UserCreationForm()
    
    # render form : form
    return render(request, 'userprofile/signup.html', {
        'form': form
    })
    
    
    
# my account view
# Django ORM query for retrieving a Team object, and selects the first item [0] from the result set
@login_required
def myaccount(request):
    team = Team.objects.filter(created_by=request.user)[0]
    
    return render(request, 'userprofile/myaccount.html', {
        'team': team
    })
