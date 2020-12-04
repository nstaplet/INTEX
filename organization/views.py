from django.shortcuts import render
from django.http import HttpResponse

def organizationWelcomPageView(request) :
    return render(request, 'applicant/organizationwelcomepage.html')