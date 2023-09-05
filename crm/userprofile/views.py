from django.shortcuts import render, redirect
# import pack with auth with pass, username, email
from django.contrib.auth.forms import UserCreationForm
# import userprofile for check information
from .models import Userprofile
from .forms import SignupForm
# for my account
from django.contrib.auth.decorators import login_required
# for team account
from team.models import Team

from .models import Userprofile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            team = Team.objects.create(name='The team name', created_by=user)
            team.members.add(user)
            team.save()
            
            Userprofile.objects.create(user=user, active_team=team)

            return redirect('/log-in/')
    else:
        form = SignupForm()

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
