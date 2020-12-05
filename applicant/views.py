from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .algorithms import display_top_skills, get_applicant_skills

def indexPageView(request) :
    return render(request, 'applicant/index.html')

def applicantlogin(request) :
    return render(request, 'applicant/applicantlogin.html')

def applicantsignup(request) :
    return render(request, 'applicant/applicantsignup.html')

def applicantwelcome(request) :

    #username = request.POST['username']
    #password = request.POST['password']

    #user = authenticate(username = username, password = password)

    #if user is not None:
        return render(request, 'applicant/applicantwelcome.html')

    #else:
    #    return render(request, 'applicant/applicantlogin.html')

def applicant_dash(request):

    top_skills = set(display_top_skills())
    applicant_skills = get_applicant_skills(request.user.id)

    context = {
        'top_skills': top_skills,
        'applicant_skills': applicant_skills,
    }

    return render(request, 'applicant/applicantdashboard.html', context)