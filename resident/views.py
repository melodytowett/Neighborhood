
import re
from django.http import request
from django.shortcuts import redirect, render
from.forms import BusinessForm, HoodForm, PostForm, ProfileForm
from resident.models import Business, Neighborhood, Post, Profile

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
            hood.admin= current_user
            hood.save()
        return redirect('hood')
    else:
        hood_form = HoodForm()
    return render(request,'all-hoods/new-hood.html',{"hood_form":hood_form})

def my_hood(request,id):
    current_user = request.user
    hood = Neighborhood.objects.get(id=id)
    businesses = Business.objects.filter(neighborhood=hood)
    # posts = Post.objects.filter(neighborhood=hood)
    ocupants = Profile.objects.filter(neighborhood=hood)
    request.user.save()
    return render(request,'all-hoods/my-hood.html',{"hood":hood,"businesses":businesses,"ocupants":ocupants,"user":current_user})

def my_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST,request.FILES)
        if prof_form.is_valid():
            profile = prof_form.save(commit=False)
            profile.user=current_user
            # profile.save()
        return redirect('view_prof')
    else:
        prof_form = ProfileForm()
    return render(request,'all-hoods/profile.html',{"prof_form":prof_form})

def view_prof(request):
    profiles = Profile.objects.all()
    return render(request,'all-hoods/view-prof.html',{"profiles":profiles})

def my_business(request,id):
    hood=Neighborhood.objects.get(id=id)
    if request.method == 'POST':
        biz_form = BusinessForm(request.POST,request.FILES)
        if biz_form.is_valid():
            business = biz_form.save(commit=False)
            business.neighborhood = hood
            business.owner = request.user
            business.save()
        return redirect('business',id)
    else:
        biz_form = BusinessForm()
    return render(request,'all-hoods/biz.html',{"biz_form":biz_form})

def my_post(request,id):
    hood = Neighborhood.objects.get(id=id)
    # current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.neighborhood = hood
            post.author = request.user
            post.save()
        return redirect('hood',id)
    else:
        post_form = PostForm()
    return render(request,'all-hoods/post.html',{"post_form":post_form})