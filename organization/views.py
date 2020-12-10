from django.shortcuts import render, redirect
from django.http import HttpResponse

# models
from django.contrib.auth import authenticate, login, logout
from .models import organization, skill, listing, listing_skills, mentor, offers_made
from person.models import applicant
from applicant.models import applicant_skills, message

from django.contrib import messages
from django.contrib.auth.models import User

# outside functions
from .algorithms import recommend_users

def organizationWelcomePageView(request) :
    # print(request.session['username'])
    # if request.session['username']:
    if request.session['currentUser']:

        applicants_data = applicant.objects.all()
        listings_data = listing.objects.all().filter(organization_id__exact=request.session['currentUser']) # need a dynamic value here
        skills_list = skill.objects.all()

        try: 
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'skills': skills_list,
                'user': request.session['currentUser'],
            }
        except Exception:
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'skills': skills_list,
                'user': 2,
            }

        return render(request, 'organization/organizationwelcome.html', context)


def organizationlogin(request):
    context = {
        'title': 'Organization Login',
        'user': None
    }
    return render(request, 'organization/organizationlogin.html', context)


def organizationsignup(request):
    context = {
        'user': None,
        'title': 'Organization Sign Up'
    }
    return render(request, 'organization/organizationsignup.html', context)


def createOrganization(request):
    company_name = request.POST.get('company_name')
    company_email = request.POST.get('company_email')
    company_password = request.POST.get('company_password')
    company_address = request.POST.get('company_address')
    size = request.POST.get('company_size')
    sectors = request.POST.get('company_sector')

    if (organization.objects.filter(company_name__exact=company_name).exists()):
        messages.info(request, 'That company name has already been claimed. Please try again.')
        return render(request, 'organization/organizationsignup.html')

    elif (organization.objects.filter(company_email__exact=company_email).exists()):
        messages.info(request, 'That company email has already been claimed. Please try again.')
        return render(request, 'organization/organizationsignup.html')

    else:
        organization.objects.create(company_name = company_name, company_email = company_email, company_address = company_address, size=size, sectors = sectors)
        User.objects.create_user(username=company_email, password = company_password)
        data = organization.objects.filter(company_email__exact=company_email)

        request.session['currentUser'] = data.first().organization_id

        applicants_data = applicant.objects.all()
        listings_data = listing.objects.all().filter(organization_id__exact=request.session['currentUser']) # need a dynamic value here
        skills_list = skill.objects.all()

        context = {
            'applicants': applicants_data,
            'listings': listings_data,
            'skills': skills_list,
            'orgInfo': data,
            'title': 'Organization Homepage',
            'user': request.session['currentUser'],
        }

        # messages.success(request, f'Account created for {company_name}!')
        return render(request, 'organization/organizationlogin.html', context)


def companyLogin(request):
    username = request.POST.get('company_email')
    password = request.POST.get('company_password')

    user = authenticate(username = username, password = password)

    if user is not None:
        data = organization.objects.all().get(company_email=username)
        request.session['currentUser'] = data.organization_id

        print(request.session['currentUser'])

        request.session['currentUser'] = data.organization_id
        applicants_data = applicant.objects.all()
        listings_data = listing.objects.all().filter(organization_id__exact=request.session['currentUser']) 
        skills_dict = {}

        app_skills = applicant_skills.objects.all()

        for app in app_skills:
            if app.applicant_id in skills_dict:
                skills_dict[app.applicant_id].append([app.skill_id, app.skill_value])

        skills_list = skill.objects.all()

        # applicants[applicant_id] = {
        #     applicant: applicant,
        #     skills: skills[],
        # }

        try: 
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'skills': skills_list,
                'user': request.session['currentUser'],
            }
        except Exception:
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'skills': skills_list,
                'user': 2,
            }
        
        return render(request, 'organization/organizationwelcome.html', context)
    else:
        context = {
            'title': 'Organization Login',
            'user': None
        }

        messages.info(request, 'You username or password is incorrect, please try again!')
        return render(request, 'organization/organizationlogin.html', context)
    

def createJobListing(request):
    if request.session['currentUser']:
        new_listing = listing()
        
        try:
            new_listing.status = request.POST.get('status')
            new_listing.city = request.POST.get('city')
            new_listing.job_title = request.POST.get('job_title')
            new_listing.contracts = request.POST.get('contracts')
            new_listing.relocation = request.POST.get('relocation')
            new_listing.description = request.POST.get('description')
            new_listing.compensation = request.POST.get('compensation')
            new_listing.organization_id = request.session['currentUser'] # int(request.POST.get('orgID'))
        
        except Exception:
            print('error')

        new_listing.save()    
        
        # if (skill.objects.filter(skill_name__iexact=skillName).exists()):
        #     skill_ob = skill.objects.all().get(skill_name__iexact=skillName)
        #     skill_id = skill_ob.skill_id 

        # try:
        #     new_listing_skill.skillName = request.POST.get('skillname')
        #     new_listing_skill.skill_value = request.POST.get('skill_value') 
        #     new_listing_skill.listing_id = new_listing.listing_id
        # except Exception:
        #     pass
        

        for i in range(10):
            new_listing_skill = listing_skills()
            if request.POST.get(f'proficiency{i}'):
                proficiency = request.POST.get(f'proficiency{i}')
                skill_name = request.POST.get(f'skillname{i}')
                print(skill_name)
                skillid = skill.objects.all().filter(skill_name__contains=skill_name)
                print(skillid)

                new_listing_skill.skill_id = skillid.first().skill_id
                new_listing_skill.skill_value = proficiency
                new_listing_skill.listing_id = new_listing.listing_id

                new_listing_skill.save()
        
        # PK from the listing object 
        # listing_id_FK = new_listing.listing_id

        # listing_skills.objects.create(
        #     skill_value = skill_value,
        #     skill_id = skill_id,
        #     listing_id = listing_id_FK
        # )

        applicants_data = applicant.objects.all()
        listings_data = listing.objects.all().filter(organization_id__exact=request.session['currentUser']) # need a dynamic value here

        context = {
            'applicants': applicants_data,
            'listings': listings_data,
            'title': 'Organization Homepage',
            'user': request.session['currentUser'],
        }

        return render(request, 'organization/organizationwelcome.html', context)
    else:
        return redirect('organizationsignup')


def companyLogout(request):
    logout(request)
    messages.info(request, "You have logged out successfully!")
    request.session['currentUser'] = None
    return redirect("index")


def viewApplicant(request, id):
    if request.session['currentUser']:
        rec_applicants = []
        try:
            print(request.session['username'])
        except Exception:
            pass
            
        try:
            items = recommend_users(89, id)
            print(id)
            for item in items:
                print(item)
                rec_applicants.append(applicant.objects.all().get(applicant_id=item))
                # rec_applicants.append(applicant.objects.all().get(applicant_id=int(item))) if the above line needs a data conversion
        except Exception:
            print('Could not retrieve recommended users')

        curr_applicant = applicant.objects.all().get(applicant_id=id)
        skill_ids = applicant_skills.objects.all().filter(applicant_id=curr_applicant.applicant_id)
        skill_names = []

        for item in skill_ids:
            skill_names.append([skill.objects.all().get(skill_id=item.skill_id), item.skill_value])

        print(type(curr_applicant.city))

        rec_applicants1 = rec_applicants[0:5]
        rec_applicants2 = rec_applicants[5:10]

        context = {
            'rec_users1': rec_applicants1,
            'rec_users2': rec_applicants2,
            'applicant': curr_applicant,
            'skill_set': skill_names,
            'title': f'Applicant: {curr_applicant.first_name} {curr_applicant.last_name}'
        }
        
        return render(request, 'organization/viewapplicant.html', context)
    else:
        return redirect('organizationsignup')
















# mentor stuff
def mentorAddPageView(request):
    # pass organization id, nothing else should be necessary
    if request.session['currentUser']:
        orgID = request.session['currentUser']

        context = {
            'orgID' : orgID,
            'title': 'Add Mentor'
        }

        return render(request, 'organization/addmentor.html', context)
    else:
        return redirect('organizationsignup')

def createMentor(request):
    # create mentor object, reroute to organizationwelcome and pass orgInfo
    if request.session['currentUser']:
        orgID = request.POST['org-ID']
        fName = request.POST['first-name']
        lName = request.POST['last-name']
        indName = request.POST['industry-name']

        orgObject = organization.objects.get(organization_id=orgID)

        mentor.objects.create(organization=orgObject, first_name=fName, last_name=lName, industry=indName)


        data = organization.objects.all().filter(organization_id__exact=orgID)

        request.session['currentUser'] = data.first().organization_id

        print(request.session['currentUser'])

        applicants_data = applicant.objects.all()
        listings_data = listing.objects.all().filter(organization_id__exact=request.session['currentUser']) 
        skills_dict = {}

        app_skills = applicant_skills.objects.all()

        for app in app_skills:
            if app.applicant_id in skills_dict:
                skills_dict[app.applicant_id].append([app.skill_id, app.skill_value])


        # applicants[applicant_id] = {
        #     applicant: applicant,
        #     skills: skills[],
        # }

        try: 
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'user': request.session['currentUser'],
                'orgInfo': data
            }
        except Exception:
            context = {
                'applicants': applicants_data,
                'listings': listings_data,
                'title': 'Organization Homepage',
                'user': 2,
                'orgInfo': data
            }
        return render(request, 'organization/organizationwelcome.html', context)
    else:
        return redirect('organizationsignup')


def viewMentors(request):
    if request.session['currentUser']:
        # orgID = request.POST['orgID']
        org = organization.objects.all().get(organization_id__exact=request.session['currentUser'])
        
        mentorData = mentor.objects.filter(organization=org.organization_id)

        context = {
            'mentors' : mentorData,
            'orgID' : org.organization_id,
            'title': f'{org.company_name} Mentors'
        }
        return render(request, 'organization/viewmentors.html', context)


def viewMessages(request):
    if request.session['currentUser']:
        mentorID = request.POST['mentorID']

        messagedata = message.objects.all().filter(mentor_id__exact=mentorID).order_by('-timesent')

        context = {
            'mentorID' : mentorID,
            'allMessages' : messagedata,
            'title': 'Mentor Messages',
        }

        return render(request, 'organization/mentormessages.html', context)
    else: 
        return redirect('organizationsignup')


def mentorCreateMessage(request):
    if request.session['currentUser']:
        mentorID = request.POST['mentorID']
        mentorID = int(mentorID)
        appSender = request.POST.get('sender')
        recipient = request.POST['recipient']
        msgContent = request.POST['content']

        recipientNames = recipient.split()

        # If recipient doesn't exist, redirect to same page with a message saying so. Refill content field so that it doesn't have to be retyped
        if applicant.objects.filter(first_name__iexact=recipientNames[0], last_name__iexact=recipientNames[1]).exists():
            appObject = applicant.objects.all().filter(first_name__iexact=recipientNames[0], last_name__iexact=recipientNames[1])
            mentorObject = mentor.objects.get(mentor_id__exact=mentorID)
            message.objects.create(mentor=mentorObject, applicant=appObject.first(), content=msgContent, sender_applicant=appSender)

            messagedata = message.objects.filter(mentor_id__exact=mentorID).order_by('-timesent')

            context = {
                'mentorID' : mentorID,
                'allMessages' : messagedata,
                'title': 'Mentor Messages',
            }

            return render(request, 'organization/mentormessages.html', context)

        else:
            messages.info(request, 'Sorry, we have no record of that applicant. Please try again.')
            # redirect to all messages page
            messagedata = message.objects.filter(mentor_id__exact=mentorID).order_by('-timesent')
            # refill message content with current content

            context = {
                'mentorID' : mentorID,
                'allMessages' : messagedata,
                'title': 'Mentor Messages',
            }

            return render(request, 'organization/mentormessages.html', context)
    else:
        return redirect('organizationsignup')


def mentorSingleMessageView(request):
    if request.session['currentUser']:
        messageID = request.POST['message-id']
        messageID = int(messageID)

        print(messageID)

        singleMessageData = message.objects.filter(message_id__exact=messageID)

        print(singleMessageData)

        context = {
            'messageobject' : singleMessageData,
            'title': f'Message to {singleMessageData.first().applicant.first_name} {singleMessageData.first().applicant.last_name}'
        }

        return render(request, 'organization/mentorsinglemessage.html', context)
    else:
        return redirect('organizationsignup')