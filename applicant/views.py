from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# get the models
from organization.models import skill, offers_made, organization, mentor, listing_skills, listing
from .models import applicant_skills, message
from person.models import applicant

# get other fucntions
from .algorithms import display_top_skills, get_applicant_skills, recommend_listings
from django.contrib import messages
from django.contrib.auth.models import User


# looking for a job / looking to hire - general index page
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

    
    request.session['user'] = None

    context = {
        'user': request.session['user']
    }

    # print(request.session['user'])

    return render(request, 'applicant/index.html', context)


def viewlisting(request, org_id, list_id):
    listings_list = []

    try:
        rec_listing_ids = recommend_listings(org_id, list_id)
        for listingid in rec_listing_ids:
            listings_list.append(listing.objects.all().get(listing_id=listingid))
    except Exception:
        print('Unable to retrieve recommendations')

    # get the main listing
    listing_main = listing.objects.all().get(listing_id=list_id)

    # get the organization name
    org_name = organization.objects.all().get(organization_id=listing_main.organization_id)

    # get the associated skills
    skills_values_objects = listing_skills.objects.all().filter(listing_id=listing_main.listing_id)
    skill_set = []

    # get the names of those skills and the value of the skill
    for skill_object in skills_values_objects:
        skill_set.append([skill.objects.all().get(skill_id=skill_object.skill_id), skill_object.skill_value])

    context = {
        'listings_rec': listings_list,
        'listing': listing_main,
        'skill_set': skill_set,
        'org': org_name,
    }

    return render(request, 'applicant/viewlisting.html', context)


def applicantloginPageView(request) :
    # print(request.session['user'])
    return render(request, 'applicant/applicantlogin.html')


def applicantsignupPage(request) :
    return render(request, 'applicant/applicantsignup.html')


def applicantLogin(request) :

    username = request.POST.get('username')
    password = request.POST.get('password')

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

        request.session['currentUser'] = user.id

        context = {
            'skills' : skillListNamesEdited,
            'applicant' : data
        }
        return render(request, 'applicant/applicantwelcome.html', context)

    else:
        print('nope')
        return render(request, 'applicant/applicantlogin.html')


def applicant_dash(request):
    print(request.session['user'])
    try: 
        print(request.user)
    except Exception:
        pass

    if not request.session['user'] is None:
        top_skills = display_top_skills(request)

        applicant_skills_list = get_applicant_skills(2)  # request.user.id

        for s in applicant_skills_list:
            if s in top_skills:
                top_skills.remove(s)

        top_skills = top_skills[0:5]

        if not isinstance(top_skills[0], str):
            top_skills_strings = []
            for item in top_skills:
                top_skills_strings.append(item.skill_name)

            context = {
                'top_skills': top_skills_strings,
                'applicant_skills': applicant_skills_list,
            }
        else:
            context = {
                'applicant': request.user,
                'top_skills': top_skills,
                'applicant_skills': applicant_skills_list,
            }

        return render(request, 'applicant/applicantdashboard.html', context)
    else:
        return render(request, 'applicant/index.html')
    

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

        request.session['currentUser'] = request.user.id # this could keep track of the users

        context = {
            'applicant' : applicantdata,
            'skills' : skillListNames
        }

        return render(request, 'applicant/applicantwelcome.html', context)


def updateSkillsPageView(request):
    if not request.session['currentUser'] is None:
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
    if not request.session['currentUser'] is None:
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
    appID = int(request.POST['applicant_id'])
    # pull all data from the messages table that has this applicant's ID
    messagedata = message.objects.filter(applicant_id__exact=appID).order_by('-timesent')

    context = {
        'appID' : appID,
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


def createMessage(request):
    appID = request.POST['app-id']
    appID = int(appID)
    appSender = request.POST.get('sender')
    recipient = request.POST['recipient']
    msgContent = request.POST['content']

    recipientNames = recipient.split()
    

    # If recipient doesn't exist, redirect to same page with a message saying so. Refill content field so that it doesn't have to be retyped
    if mentor.objects.filter(first_name__iexact=recipientNames[0], last_name__iexact=recipientNames[1]).exists():
        mentorObject = mentor.objects.get(first_name__iexact=recipientNames[0], last_name__iexact=recipientNames[1])
        appObject = applicant.objects.get(applicant_id__exact=appID)
        message.objects.create(mentor=mentorObject, applicant=appObject, content=msgContent, sender_applicant=appSender)

        messagedata = message.objects.filter(applicant_id__exact=appID).order_by('-timesent')

        context = {
            'appID' : appID,
            'allMessages' : messagedata
        }

        return render(request, 'applicant/messages.html', context)

    else:
        messages.info(request, 'Sorry, we have no record of that mentor. Please try again.')
        # redirect to all messages page
        messagedata = message.objects.filter(applicant_id__exact=appID).order_by('-timesent')
        # refill message content with current content

        context = {
            'appID' : appID,
            'allMessages' : messagedata
        }

        return render(request, 'applicant/messages.html', context)

def applicantLogout(request):
    logout(request)
    # messages.info(request, "You have logged out successfully!")
    return redirect("index")
