from django.shortcuts import render
from django.http import HttpResponse

def organizationWelcomePageView(request) :
    return render(request, 'organization/organizationwelcomepage.html')

def organizationlogin(request) :
    return render(request, 'organization/organizationlogin.html')

def organizationsignup(request) :
    return render(request, 'organization/organizationsignup.html')