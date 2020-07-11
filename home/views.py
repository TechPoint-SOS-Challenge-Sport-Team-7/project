from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, _get_queryset
from .models import Information


def home(response):
    return render(response, "home/home.html", {})

def roster(response):
    print('got here')
    return render(response, "home/roster.html", {})

def videos(response):
    return render(response, "home/videos.html", {})

def calendar(response):
    return render(response, "home/calendar.html", {})

def store(response):
    return render(response, "home/store.html", {})

def drivein(response):
    return render(response, "home/drivein.html", {})

def questions(response):
    return render(response, "home/questions.html", {})
