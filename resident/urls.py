from unicodedata import name
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .import views 

urlpatterns=[
    path('',views.home,name='home'),
    path('new_hood/',views.join_hood,name='new_hood'),
    path('hood/',views.my_neighborhood,name='hood'),
    path('my_profile/<username>/',views.my_profile,name='profile'),
    path('view-prof/',views.view_prof,name='view_prof'),
    path('business/',views.my_business,name='business'),
    path('view_biz/',views.view_biz,name='my_biz'),
    path('my_post/',views.my_post,name='post'),
    path('hood_post/',views.hood_post,name='hood_posts')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)