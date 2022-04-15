from unicodedata import name
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .import views 

urlpatterns=[
    path('',views.home,name='home'),
    path('hood/',views.my_neighborhood,name='hood'),
    path('new_hood/',views.join_hood,name='new_hood'),
    path('my_profile/<username>/',views.my_profile,name='profile'),
    path('view-prof',views.view_prof,name='view_prof'),
    path('neighbors/',views.my_hood,name='neighbors'),
    path('my_biz/',views.my_business,name='business'),
    path('my_post',views.my_post,name='post')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)