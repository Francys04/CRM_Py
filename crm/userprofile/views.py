from django.shortcuts import render, redirect
# import pack with auth with pass, username, email
from django.contrib.auth.forms import UserCreationForm
# import userprofile for check information
from .models import Userprofile

# Create your views here.

def signup(request):
    # check if the form has been submited
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # if info is correct
        if form.is_valid():
            user = form.save()
            Userprofile.objects.create(user=user)
            
            return redirect('/log_in')
        # if not post request
        else:
            form = UserCreationForm()
        
    form = UserCreationForm()
    
    # render form : form
    return render(request, 'userprofile/signup.html', {
        'form': form
    })
