from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from . import views
from .views import videos


urlpatterns = [
    path('', views.home, name = 'home'),
    path('roster/', views.roster, name = 'roster'),
    path('videos/', views.videos, name = 'videos'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('store/', views.store, name = 'store'),
    path('drivein/', views.drivein, name='drive-in'),
    path('drivein/confirmation', views.confirmation, name='confirmation'),
    path('settings/', views.settings, name='settings'),
    path('error/', views.error, name='error'),
    path('about/', views.about, name='about')

]