from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from .email import send_email
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import request
from django.contrib.auth .decorators import login_required
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

def login_user(request):
    if request.method =='POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"invalid uername or password")
    form = AuthenticationForm()
    return render(request=request,template_name="register/login.html",context={"login_form":form})

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
    
@login_required(login_url='login')
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

@login_required(login_url='login')
def my_neighborhood(request):
    current_user = request.user
    neighbors = Neighborhood.objects.all()
    posts = Post.objects.all()
    return render(request,'all-hoods/hood.html',{"neighbors":neighbors,"posts":posts,"current_user":current_user})

@login_required(login_url='login')
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

@login_required(login_url='login')
def view_prof(request):
    profiles = Profile.objects.all()
    return render(request,'all-hoods/view-prof.html',{"profiles":profiles})

@login_required(login_url='login')
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

@login_required(login_url='login')
def view_biz(request):
    businesses = Business.objects.all()
    neighbors = Neighborhood.objects.all()
    return render(request,'all-hoods/business.html',{"businesses":businesses,"neighbors":neighbors})

@login_required(login_url='login')
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

@login_required(login_url='login')
def hood_post(request):
    current_user = request.user
    posts = Post.objects.all()
    return render(request,'all-hoods/view-posts.html',{"user":current_user,"posts":posts})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

@login_required(login_url='login')
def leave_hood(request,id):
    hood = Neighborhood.objects.get(id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='login')
def search_hood(request):
    current_user = request.user
    if request.method == 'GET':
        name = request.GET.get("name")
        hoods = Neighborhood.objects.filter(name__icontains=name).all()
    return render(request,'all-hoods/search.html',{"hoods":hoods,"current_user":current_user})