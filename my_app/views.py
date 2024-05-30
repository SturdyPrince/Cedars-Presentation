from django.shortcuts import render, redirect
from django.contrib.auth import login
from . forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, ('registration/signup.html'))


def signin(request):
    return render(request, ('registration/signin.html'))