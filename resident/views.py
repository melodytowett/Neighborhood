from unicodedata import name
from django.shortcuts import redirect, render

from resident.models import Neighborhood

# Create your views here.
def home(request):
    return render(request,'home.html')

def my_neighborhood(request):
    neighbors = Neighborhood.objects.all()
    return render(request,'all-hoods/hood.html',{"neighbors":neighbors})