from django.shortcuts import render

"""This functions define view render templates to display the content of the 'core/index.html' and 
'core/about.html' templates, respectively."""

def index(request):
    return render(request, 'core/index.html')

# about info
def about(request):
    return render(request, 'core/about.html')