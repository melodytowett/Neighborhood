from unicodedata import name
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .import views 

urlpatterns=[
    path('',views.home,name='home'),
    path('hood/',views.my_neighborhood,name='hood'),
    path('new_hood/',views.join_hood,name='new_hood'),
    path('my_profile/',views.my_profile,name='profile'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)