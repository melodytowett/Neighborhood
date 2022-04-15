from dataclasses import field, fields
from .models import Business, Neighborhood, Post, Profile
from django import forms
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
        fields = ['business_name','business_image','email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','post']
