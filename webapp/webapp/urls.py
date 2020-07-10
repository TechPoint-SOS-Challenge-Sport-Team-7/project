from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('fan/', include('home.urls')), 
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('', include('intro.urls')),
]
