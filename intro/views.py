from django.shortcuts import render


def intro(response):
    return render(response, "intro/base.html", {})