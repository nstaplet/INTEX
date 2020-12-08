from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# get the models
from organization.models import skill, offers_made, organization, mentor, listing_skills, listing
from .models import applicant_skills, message
from person.models import applicant

# get other fucntions
from .algorithms import display_top_skills, get_applicant_skills
from django.contrib import messages
from django.contrib.auth.models import User



def indexPageView(request) :

    # applicants = applicant.objects.all()
    # organizations = organization.objects.all()
    # skills = skill.objects.all()
    # offers = offers_made.objects.all()
    # applicant_skills_lst = applicant_skills.objects.all()
    # messages = message.objects.all()
    # mentors = mentor.objects.all()
    # listing_skills_lst = listing_skills.objects.all()
    # listings = listing.objects.all()

    # context = {
    #     'applicants': applicants,
    #     'organizations': organizations,
    #     'skills': skills,
    #     'offers': offers,
    #     'applicant_skills': applicant_skills_lst,
    #     'messages': messages,
    #     'mentors': mentors,
    #     'listings_skills': listing_skills_lst,
    #     'listings': listings,
    # }

    return render(request, 'applicant/index.html')

def applicantloginPageView(request) :
    return render(request, 'applicant/applicantlogin.html')

def applicantsignupPage(request) :
    return render(request, 'applicant/applicantsignup.html')


def applicantLogin(request) :

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    if user is not None:
        data = applicant.objects.filter(username__exact=username)
        
        appInfo = applicant.objects.filter(username__exact=username).values_list('applicant_id', flat=True)[0]
        skilldata = applicant_skills.objects.filter(applicant__exact=appInfo)
        skillListNames = []
        skillListNamesEdited = []

        for skillitem in skilldata:
            skillListNames.append( skill.objects.filter(skill_id__exact=skillitem.skill_id).values_list('skill_name', flat=True)[0] )
        for skillname in skillListNames:
            skillname = skillname[6:len(skillname)]
            skillname = skillname.capitalize()
            skillListNamesEdited.append(skillname)

        context = {
            'skills' : skillListNamesEdited,
            'applicant' : data
        }
        return render(request, 'applicant/applicantwelcome.html', context)

    else:
       return render(request, 'applicant/applicantlogin.html')



def applicant_dash(request):

    top_skills = display_top_skills()

    applicant_skills_list = get_applicant_skills(2)  # request.user.id

    for s in applicant_skills_list:
        if s in top_skills:
            top_skills.remove(s)

    context = {
        'top_skills': top_skills[0:5],
        'applicant_skills': applicant_skills_list,
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

        return render(request, 'applicant/applicantsignup.html')

    elif (applicant.objects.filter(username__exact=email).exists()):
        messages.info(request, 'That username has already been claimed. Please try again.')

        return render(request, 'applicant/applicantsignup.html')

    else:
        applicant.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, city=city, email_opt_in=email_opt_in)
        User.objects.create_user(username=username, email=email, password=password)
        
            # return render(request, 'applicant/applicantsignup.html')
        
        applicantdata = applicant.objects.filter(username__exact=username)
        applicantdataid = applicant.objects.filter(email__exact=email).values_list('applicant_id', flat=True)[0]
        skilldata = applicant_skills.objects.filter(applicant__exact=applicantdataid)
        skillListNames = []

        for skillitem in skilldata:
            skillListNames.append(skill.objects.filter(skill_id__exact=skillitem.skill).values_list('skill_name', flat=True)[0] )

        context = {
            'applicant' : applicantdata,
            'skills' : skillListNames
        }

        return render(request, 'applicant/applicantwelcome.html', context)

def updateSkillsPageView(request):
    appID = request.POST['applicant_id']

    data = skill.objects.all().distinct('skill_name')
    editdata = []
    for skill_name in data:
        editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
    context = {
        'skills' : editdata,
        'appID' : int(appID)
    }

    return render(request, 'applicant/updateskills.html', context)

def updateSkills(request):
    skills = request.POST['skillsinput']
    appID = request.POST['applicant_id']

    skills = skills.split()
    try:
        for skillitem in skills:
            skillitem = 'skill_' + skillitem
            applicant_skills.objects.create(
                skill=skill.objects.get(skill_name__iexact=skillitem),
                applicant=applicant.objects.get(applicant_id__exact=appID)
            )
    # If the skill does not exist yet, reroute to the same page
    except IndexError:
        messages.info(request, 'That skill is not currently in use.')
        data = skill.objects.all()
        editdata = []
        for skill_name in data:
            editdata.append(skill_name.skill_name[6:len(skill_name.skill_name)])
        context = {
            'skills' : editdata
        }
        return render(request, 'applicant/updateskills.html', context)


    # applicantdataid = applicant.objects.filter(email__exact=email).values_list('applicant_id', flat=True)[0]
    applicantdata = applicant.objects.filter(applicant_id__exact=appID)
    skilldata = applicant_skills.objects.filter(applicant__exact=appID)
    skillListNames = []
    skillListNamesEdited = []

    for skillitem in skilldata:
        skillListNames.append( skill.objects.filter(skill_id__exact=skillitem.skill_id).values_list('skill_name', flat=True)[0] )
    for skillname in skillListNames:
        skillname = skillname[6:len(skillname)]
        skillname = skillname.capitalize()
        skillListNamesEdited.append(skillname)

    context = {
        'skills' : skillListNamesEdited,
        'applicant' : applicantdata
    }

    return render(request, 'applicant/applicantwelcome.html', context)

def offersPageView(request):
    appID = request.POST['applicant_id']
    organizationdata = organization.objects.all()

    offers_madedata = offers_made.objects.filter(applicant__exact=appID)
    context = {
        'allOffers' : offers_madedata,
        'allOrganizations' : organizationdata
    }

    # context needs to be all offers_made objects that have this applicants primary key as a foreign key
    return render(request, 'applicant/applicantoffers.html', context)


def messagesPageView(request):
    appID = request.POST['applicant_id']
    # pull all data from the messages table that has this applicant's ID
    messagedata = message.objects.filter(applicant_id__exact=appID)

    context = {
        'appID' : int(appID),
        'allMessages' : messagedata
    }

    return render(request, 'applicant/messages.html', context)


def singleMessageView(request):
    messageID = request.POST['message-id']
    messageID = int(messageID)

    singleMessageData = message.objects.filter(message_id__exact=messageID)
    context = {
        'messageobject' : singleMessageData
    }

    return render(request, 'applicant/singlemessage.html', context)