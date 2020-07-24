from django.shortcuts import render, redirect
from .forms import RegisterForm, login


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/logout")
    else:
            form = RegisterForm()
    return render(response, "register/register.html", {"form":form})