from django.shortcuts import render

# Create your views here.
from .models import project


# Create your views here.
def homepage(request):
    projects = project.objects.all() #take from project DB
    return render(request, 'projects/index.html', {'projects': projects})


