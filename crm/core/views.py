from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

# about info
def about(request):
    return render(request, 'core/about.html')