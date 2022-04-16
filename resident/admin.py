from re import A
from django.contrib import admin

from resident.models import Business, Neighborhood, Post, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Post)