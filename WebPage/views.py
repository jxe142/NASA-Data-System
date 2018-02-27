from django.shortcuts import render, redirect
from .models import NasaFiles, FileType
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
import os, json
from django.conf import settings

@login_required
def logOut(request):
    print('You are logging out')
    logout(request)
    print('Logged out')
    return redirect('/login')


# NOTE TODO --> REMOVE ALL THE DEFAULT PERMISSIONS FROM USERS
def register(request):
    print('Registation')
    #Note the email will be the userName and the email

    context = {}
    context['usernameNotAvailable'] = False

    if(request.POST):

        userName = request.POST.get('username')
        password = request.POST.get('password')
        firstN = request.POST.get('firstN')
        lastN = request.POST.get('lastN')
        isPaid = request.POST.get('paid')


        print(userName)

        #Get the free user group and add permissions
        userType = ContentType.objects.get_for_model(User)
        freeUser, created = Group.objects.get_or_create(name='Free Users')
        downloadFreeFiles, created = Permission.objects.get_or_create(name='Free Files',codename='freeF', content_type=userType)
        freeUser.permissions.add(downloadFreeFiles)

        if(User.objects.filter(username=userName).exists()):
            context['usernameNotAvailable'] = True
            return render(request, 'register.html', context=context)


        else:
            #If wer get everything from the request
            if( all((userName, password, firstN, lastN))):
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

                login(user=newUser, request=request)

                return redirect("/home", request=request)
            else:
                return HttpResponse(400, 'Please include all of the informaiton')

    return render(request, 'register.html', context=context)


@csrf_exempt
def checkUserName(request):
    if (request.POST):
        data = {}

        userName = request.POST.get('username')
        if (User.objects.filter(username=userName).exists()):
            data['available'] = False
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            data['available'] = True
            return HttpResponse(json.dumps(data), content_type='application/json')



# Used to let users update their subscription to the site
# @login_required
def home(request):
    freeUser, created = Group.objects.get_or_create(name='Free Users')
    paidUser, created = Group.objects.get_or_create(name='Paid User')
    user = request.user
    context_dict = {}



    if user.is_authenticated: #This means they are logged in
        Groups = user.groups.all()
        if paidUser in Groups: #Get the paid objects
            figType = FileType.objects.get(fileTypeName = 'Fig Files')
            speType = FileType.objects.get(fileTypeName= 'SPE Files')
            figFiles = NasaFiles.objects.filter(type=figType).order_by('name')
            speFiles = NasaFiles.objects.filter(type=speType).order_by('name')

            context_dict['figFiles'] = figFiles
            context_dict['speFiles'] = speFiles
            context_dict['paid'] = True
            print("Got paid files")

        crossType = FileType.objects.get(fileTypeName = 'Cross Sections')
        dataType = FileType.objects.get(fileTypeName='Data Sheets')
        crossFiles = NasaFiles.objects.filter(type=crossType).order_by('name')
        dataFiles = NasaFiles.objects.filter(type=dataType).order_by('name')
        context_dict['crossFiles'] = crossFiles
        context_dict['dataFiles'] = dataFiles
        print("Got free files")

    # file = NasaFiles.objects.get(pk=1118)
    # print(file.file)
    # context_dict['file'] = file.file

    return render(request, 'index.html', context=context_dict)


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

    else:
        print(request.method)

    return render(request, 'license.html')


def makeFileObjects(request):

    if(FileType.objects.filter(fileTypeName="General")): #if all files have been made take them home
        return redirect("/home", request)
    elif(request.user.is_superuser):
        rootDir = settings.MEDIA_ROOT
        request = 'http://localhost:8000/media'

        for dirName, subdirList, fileList in os.walk(rootDir):
            print('Found directory: %s' % dirName)
            path = dirName
            rPath = path.split("media")

            if rPath[1] != "":
                typeName = rPath[1].replace("/","")
                currentType = FileType()
                currentType.fileTypeName = typeName
                currentType.save()
            else:
                currentType = FileType()
                currentType.fileTypeName = "General"
                currentType.save()

            #here we make the file object for each of the objects
            for fname in fileList:

                if(rPath[1] == ""):
                    pass
                    print(fname)
                    print(rPath)
                    currentFile = NasaFiles()
                    currentFile.name = fname
                    currentFile.file = fname
                    currentFile.type = currentType
                    currentFile.save()
                else:
                    pass
                    print(rPath)
                    print(fname)
                    currentFile = NasaFiles()
                    currentFile.name = fname
                    currentFile.file = rPath[1] + '/'+ fname
                    currentFile.type = currentType
                    currentFile.save()

        return HttpResponse(200, 'It worked')
    else:
        return redirect("/home", request)



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