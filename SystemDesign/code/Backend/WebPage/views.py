from django.shortcuts import render
from .models import NasaFiles
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from django.http import HTTPResponse

#used to let users register
def register(request):
    pass


#Used to let users update their subscription to the site
@login_required
def updateSub(request):
    print('we are in')
    return render(request, 'home.html')
