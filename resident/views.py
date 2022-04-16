from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.http import request
from django.shortcuts import redirect, render
from.forms import BusinessForm, HoodForm, PostForm, ProfileForm
from resident.models import Business, Neighborhood, Post, Profile

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register/register.html", context={"register_form":form})

def home(request):
    return render(request,'home.html')

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
    
def my_neighborhood(request):
    current_user = request.user
    neighbors = Neighborhood.objects.all()
    posts = Post.objects.all()
    return render(request,'all-hoods/hood.html',{"neighbors":neighbors,"posts":posts,"current_user":current_user})


def my_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if prof_form.is_valid():
            profile = prof_form.save(commit=False)
            profile.user=current_user
            profile.save()
            return redirect('view_prof')
    else:
        prof_form = ProfileForm(instance=request.user.profile)
    return render(request,'all-hoods/profile.html',{"prof_form":prof_form})

def view_prof(request):
    profiles = Profile.objects.all()
    return render(request,'all-hoods/view-prof.html',{"profiles":profiles})

def my_business(request):
    # hood=Neighborhood.objects.get(id=id)
    current_user = request.user
    businesses = Business.objects.all()
    if request.method == 'POST':
        biz_form = BusinessForm(request.POST,request.FILES)
        if biz_form.is_valid():
            business = biz_form.save(commit=False)
            # business.neighborhood = businesses
            business.owner = current_user
            business.save()
            return redirect('my_biz')
    else:
        biz_form = BusinessForm()
    return render(request,'all-hoods/biz.html',{"biz_form":biz_form,"businesses":businesses})

def view_biz(request):
    businesses = Business.objects.all()
    neighbors = Neighborhood.objects.all()
    return render(request,'all-hoods/business.html',{"businesses":businesses,"neighbors":neighbors})

def my_post(request):
    # hood = Neighborhood.objects.get(id=id)
    current_user = request.user
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            # post.neighborhood = hood
            post.author = request.user
            post.save()
            return redirect('hood')
    else:
        post_form = PostForm()
    return render(request,'all-hoods/post.html',{"post_form":post_form})
def hood_post(request):
    current_user = request.user
    posts = Post.objects.all()
    return render(request,'all-hoods/view-posts.html',{"user":current_user,"posts":posts})
