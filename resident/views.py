from locale import currency
from unicodedata import name
from django.shortcuts import redirect, render
from.forms import BusinessForm, HoodForm, ProfileForm
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

def my_profile(request):
    current_user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST,request.FILES)
        if prof_form.is_valid():
            profile = prof_form.save(commit=False)
            profile.user=current_user
            profile.save()
        return redirect('new_hood')
    else:
        prof_form = ProfileForm()
    return render(request,'all-hoods/profile.html',{"prof_form":prof_form})
        
def my_business(request):
    current_user = request.user
    if request.method == 'POST':
        biz_form = BusinessForm(request.POST,request.FILES)
        if biz_form.is_valid():
            business = biz_form.save(commit=False)
            business.user = current_user
            business.save()
        return redirect('business')
    else:
        biz_form = BusinessForm()
    return render(request,'all-hoods/biz.html',{"biz_form":biz_form})

