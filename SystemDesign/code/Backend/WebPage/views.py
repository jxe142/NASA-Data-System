from django.shortcuts import render, redirect
from .models import NasaFiles
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.http import HTTPResponse

#Used to allow people to login
# def login(request):
        
#     if request.POST:


#         userName = request.POST.get('username')
#         password = request.POST.get('password')
#         currentUser = authenticate(request, username=userName, password=password)
#         if currentUser is not None:
#             login(request, currentUser)
#             #And redirect the user to the home page

#         #Try to login with the email  
#         else: 
#             email = request.POST['email']
#             currentUser = authenticate(request, email=email, password=password)
#             if currentUser is not None:
#                 login(request, currentUser)

#             #The user doesnt exist
#             else:
#                 return HTTPResponse(401, 'Username, Email or Password failed try again')

#     return render(request, 'login.html')

@login_required
def logOut(request):
    print('You are logging out')
    logout(request)
    print('Logged out')
    return redirect('/login')


#used to let users register
def register(request):
    pass


#Used to let users update their subscription to the site
# @login_required
def updateSub(request):
    print('We are home')
    return render(request, 'home.html')
