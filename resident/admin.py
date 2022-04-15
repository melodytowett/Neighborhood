from re import A
from django.contrib import admin

from resident.models import Neighborhood, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Neighborhood)