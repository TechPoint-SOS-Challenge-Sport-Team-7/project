from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('roster/', views.roster, name = 'roster'),
    path('videos/', views.videos, name = 'videos'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('store/', views.store, name = 'store'),
]