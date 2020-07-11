from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('roster/', views.roster, name = 'roster'),
    path('videos/', views.videos, name = 'videos'),
    path('calendar/', views.calendar, name = 'calendar'),
    path('store/', views.store, name = 'store'),
    path('drivein/', views.drivein, name='drive-in'),
    path('questions/', views.questions, name='question and answers'),

]