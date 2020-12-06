from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .algorithms import display_top_skills, get_applicant_skills
from organization.models import skill
from person.models import applicant
from django.contrib import messages
from .models import applicant_skills

def indexPageView(request) :
    return render(request, 'applicant/index.html')

def applicantloginPage(request) :
    return render(request, 'applicant/applicantlogin.html')

def applicantsignupPage(request) :
    data = applicant.objects.all()
    
    context = {
        'skills' : data
    }

    return render(request, 'applicant/applicantsignup.html', context)

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


def createApplicant(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    city = request.POST['city']
    email_opt_in = request.POST.get('email_opt_in', False)
    skills = request.POST['skillsinput']

    if (applicant.objects.filter(email__exact=email).exists()):
        messages.info(request, 'That email has already been claimed. Please try again.')
        return render(request, 'applicant/applicantsignup.html')
    elif (applicant.objects.filter(username__exact=email).exists()):
        messages.info(request, 'That username has already been claimed. Please try again.')
        return render(request, 'applicant/applicantsignup.html')
    else:
        applicant.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, city=city, email_opt_in=email_opt_in,
        # password=password
        )
        skills = skills.split()
        try:
            for skillitem in skills:
                applicant_skills.objects.create(
                    applicant_id=applicant.objects.filter(email__exact=email).values_list('id', flat=True)[0],
                    skill_id=skill.objects.filter(skill_name__iexact=skillitem).values_list('skill_id', flat=True)[0]
                )
        except IndexError:
            messages.info(request, 'That skill is not currently in use.')
            return render(request, 'applicant/applicantsignup.html')
            
        applicantdata = applicant.objects.filter(email__exact=email)
        skilldata = applicant_skills.objects.filter(applicant_id__exact=applicantdata.id)
        skillListNames = []

        for skillitem in skilldata:
            skillListNames.append( skill.objects.filter(skill_id__exact=skillitem.skill_id).values_list('skill_name', flat=True)[0] )

        context = {
            'applicant' : applicantdata,
            'skills' : skillListNames
        }

        return render(request, 'applicant/applicantdashboard.html', context)