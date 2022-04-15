from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .import views 

urlpatterns=[
    path('',views.home,name='home'),
    path('hood/',views.my_neighborhood,name='hood')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)