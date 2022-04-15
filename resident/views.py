from unicodedata import name
from django.shortcuts import redirect, render
from.forms import HoodForm
from resident.models import Neighborhood

# Create your views here.
def home(request):
    return render(request,'home.html')

def my_neighborhood(request):
    neighbors = Neighborhood.objects.all()
    return render(request,'all-hoods/hood.html',{"neighbors":neighbors})

def join_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST,request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user= current_user
            hood.save()
        return redirect('hood')
    else:
        hood_form = HoodForm()
    return render(request,'all-hoods/new-hood.html',{"hood_form":hood_form})


        

