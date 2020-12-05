from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'applicant/index.html')

def applicantlogin(request) :
    return render(request, 'applicant/applicantlogin.html')

def applicantsignup(request) :
    return render(request, 'applicant/applicantsignup')

def applicantwelcome(request) :
    return render(request, 'applicant/applicantwelcome')