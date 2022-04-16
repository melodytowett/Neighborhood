
from email.policy import default
from os import name
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from cloudinary.models import CloudinaryField
# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="hood",null=True)
    about = models.TextField()
    image_hood = CloudinaryField('image',default=True)
    administrator = models.CharField(max_length=200,null=True)
    doctor_no = PhoneField(blank=True)
    police_num = PhoneField(blank=True)
    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} hood'

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def update_hood(self):
        self.update()
        
    
    @classmethod
    def my_neighbor(cls,name):
        neighbors = cls.objects.filter(name=name)
        return neighbors
    @classmethod
    def find_hood(cls,neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='prof')
    bio = models.TextField(max_length=500,blank=True)
    name = models.CharField(max_length=100,blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='hood',blank=True)
    phone = PhoneField(blank=True,help_text ='Contact phone number')
    profile_pic = CloudinaryField('image',default=True)


    def __str__(self):
        return f'{self.user.username}Profile'

    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    business_image= CloudinaryField('image',blank=True)
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE, related_name='neighborhood')
    email=models.EmailField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.business_name}Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    title = models.CharField(max_length=100)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,default=True)
    post = models.TextField(max_length=500,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    # post_date = models.DateField()

    def __str__(self):
        return f'{self.title}Post'
    
    def save_post(self):
        self.save()
    
    def delete_post(self):
        self.delete()

  