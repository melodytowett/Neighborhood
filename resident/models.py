from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name="hood",null=True)
    about = models.TextField()
    administrator = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='prof')
    bio = models.TextField(max_length=500,blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='hood',blank=True)