from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .algorithms import display_top_skills, get_applicant_skills
from organization.models import skill, offers_made
from person.models import applicant
from django.contrib import messages
from .models import applicant_skills

def indexPageView(request) :
    return render(request, 'applicant/index.html')

def applicantloginPage(request) :
    return render(request, 'applicant/applicantlogin.html')

def applicantsignupPage(request) :
    return render(request, 'applicant/applicantsignup.html')

def applicantwelcome(request) :

    #username = request.POST['username']
    #password = request.POST['password']

    #user = authenticate(username = username, password = password)

    

    #if user is not None:
        # data = applicant.objects.filter(username__exact=username)
        # context = {
            # 'applicant' : data
        # }
        return render(request, 'applicant/applicantwelcome.html'
        # , context
        )

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
    

    if (applicant.objects.filter(email__exact=email).exists()):
        messages.info(request, 'That email has already been claimed. Please try again.')

        data = skill.objects.all()
        editdata = []
        for skill_name in data:
            editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
        context = {
            'skills' : editdata
        }

        return render(request, 'applicant/applicantsignup.html', context)

    elif (applicant.objects.filter(username__exact=email).exists()):
        messages.info(request, 'That username has already been claimed. Please try again.')

        data = skill.objects.all()
        editdata = []
        for skill_name in data:
            editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
        context = {
            'skills' : editdata
        }

        return render(request, 'applicant/applicantsignup.html', context)

    else:
        applicant.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, city=city, email_opt_in=email_opt_in,
        # password=password
        )
        
                        
            # return render(request, 'applicant/applicantsignup.html')
        
        applicantdata = applicant.objects.filter(username__exact=username)
        applicantdataid = applicant.objects.filter(email__exact=email).values_list('applicant_id', flat=True)[0]
        skilldata = applicant_skills.objects.filter(applicant_id__exact=applicantdataid)
        skillListNames = []

        for skillitem in skilldata:
            skillListNames.append( skill.objects.filter(skill_id__exact=skillitem.skill_id).values_list('skill_name', flat=True)[0] )

        context = {
            'applicant' : applicantdata,
            'skills' : skillListNames
        }

        return render(request, 'applicant/applicantwelcome.html', context)


def updateSkillsPageView(request):
    data = skill.objects.all()
    editdata = []
    for skill_name in data:
        editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
    context = {
        'skills' : editdata
    }


def updateSkills(request):
    skills = request.POST['skillsinput']

    skills = skills.split()
    try:
        for skillitem in skills:
            skillitem = 'skill_' + skillitem
            applicant_skills.objects.create(
                applicant_id=applicant.objects.get(email__exact=email),
                skill_id=skill.objects.get(skill_name__iexact=skillitem)
            )
    except IndexError:
        messages.info(request, 'That skill is not currently in use.')

        data = skill.objects.all()
        editdata = []
        for skill_name in data:
            editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
        context = {
            'skills' : editdata
        }

        return render(request, 'applicant/applicantsignup.html', context)



def offersPageView(request):
    appID = applicant.objects.filter()
    data = offers_made.objects.filter()


