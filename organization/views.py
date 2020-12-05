from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def organizationWelcomePageView(request) :

    #username = request.POST['username']
    #password = request.POST['password']

    #user = authenticate(username = username, password = password)

    #if user is not None:
        return render(request, 'organization/organizationwelcome.html')

    #else:
    #    return render(request, 'organization/organizationlogin.html')

def organizationlogin(request) :
    return render(request, 'organization/organizationlogin.html')

def organizationsignup(request) :
    return render(request, 'organization/organizationsignup.html')