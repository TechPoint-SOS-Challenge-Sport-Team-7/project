from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
#from .home import views

urlpatterns = [
    path('fan/', include('home.urls')), 
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', include('django.contrib.auth.urls')),
    path('',include('intro.urls') )
]
