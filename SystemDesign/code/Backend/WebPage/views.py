from django.shortcuts import render, redirect
from .models import NasaFiles
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType

# Used to allow people to login
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


@csrf_exempt
# NOTE TODO --> REMOVE ALL THE DEFAULT PERMISSIONS FROM USERS
def register(request):
    print('Registation')
    #Note the email will be the userName and the email

    if(request.POST):

        userName = request.POST.get('username')
        password = request.POST.get('password')
        firstN = request.POST.get('firstN')
        lastN = request.POST.get('lastN')
        isPaid = request.POST.get('paid')

        #Get the free user group and add permissions
        userType = ContentType.objects.get_for_model(User)
        freeUser, created = Group.objects.get_or_create(name='Free Users')
        downloadFreeFiles, created = Permission.objects.get_or_create(name='Free Files',codename='freeF', content_type=userType)
        freeUser.permissions.add(downloadFreeFiles)

        #If wer get everything from the request
        if(userName, password, firstN, lastN):
            #make the new user
            newUser = User()
            newUser.username = userName
            newUser.email = userName
            newUser.set_password(password)
            newUser.first_name = firstN
            newUser.last_name = lastN
            newUser.save()

            print('Made the user')

            #Add them to the free group
            freeUser.user_set.add(newUser)
            print('Added to free users')
            
            #If they have paid add them to the paid group
            if(isPaid == True):
                paidUser, created = Group.objects.get_or_create(name='Paid User')
                downloadPaidFiles, created = Permission.objects.get_or_create(name='Paid Files',codename='paidF',content_type=userType)
                paidUser.permissions.add(downloadPaidFiles)
                paidUser.permissions.add(downloadFreeFiles)
                paidUser.user_set.add(newUser)
                print('Added to paid group')
        else:
            return HttpResponse(400, 'Please include all of the informaiton')
    
    return HttpResponse(200, 'User Has Been made')





# Used to let users update their subscription to the site
# @login_required
def home(request):
    print('We are home')
    return render(request, 'home.html')

@csrf_exempt
@login_required
def updateSub(request):
    if request.method == 'POST':
        print('POST')
        user = None
        if request.user.is_authenticated:
            #Take the user payment
            user = request.user

            #Add the user to the paid group
            paidUser, created = Group.objects.get_or_create(name='Paid User') 
            paidUser.user_set.add(user)
            print('Added to the group')

            return HttpResponse(200, 'You are now a paid user')
    else:
        print(request.method)

    return HttpResponse(400, 'You need to be logined in order to gain a licences')


 

