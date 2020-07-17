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

def settings(response):
    return render(response, "home/settings.html", {})

def confirmation(response):
    if (response.POST):
        login_data = response.POST.dict()
        movie = login_data.get("movieSelect")
        lot = login_data.get("lotSelect")
        print(movie, lot)
        if movie == 'select' or lot == 'select':
            return HttpResponse('Not enough information. Go back and make sure all fields are filled out!')
        else:
            context = {'movie': movie, 'lot': lot}
            return render(response, "home/confirmation.html", context)
    else:
        return render(response, "base.html")
