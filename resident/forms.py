from curses.ascii import US
from dataclasses import field
import email
from .models import Business, Neighborhood, Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['admin']
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','neighborhood','bio','phone','profile_pic']
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business_name','business_image','email','owner','neighborhood']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post','hood','author']
