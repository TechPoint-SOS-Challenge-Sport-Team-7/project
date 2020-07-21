from django.urls import path

from . import views
from .views import video

urlpatterns = [
    path('', views.home, name = 'home'),
    path('roster/', views.roster, name = 'roster'),
    path('videos/', views.video),
    path('calendar/', views.calendar, name = 'calendar'),
    path('store/', views.store, name = 'store'),
]