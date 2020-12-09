from django.shortcuts import render, redirect
from django.http import HttpResponse

# models
from django.contrib.auth import authenticate, login, logout
from .models import organization, skill, listing, listing_skills, mentor, offers_made
from person.models import applicant
from applicant.models import applicant_skills

from django.contrib import messages
from django.contrib.auth.models import User

# outside functions
from .algorithms import recommend_users

def organizationWelcomePageView(request) :
    # print(request.session['username'])
    # if request.session['username']:
    applicants = applicant.objects.all()

    context = {
        'applicants': applicants,
        'title': 'Organization Homepage',
        'user': request.session['username'],
    }

    return render(request, 'organization/organizationwelcome.html', context)


def organizationlogin(request) :
    return render(request, 'organization/organizationlogin.html')


def organizationsignup(request) :
    return render(request, 'organization/organizationsignup.html')


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
        context = {'orgInfo': data}
        # messages.success(request, f'Account created for {company_name}!')
        return render(request, 'organization/organizationlogin.html', context)


def companyLogin(request):
    username = request.POST.get('company_email')
    password = request.POST.get('company_password')

    user = authenticate(username = username, password = password)

    if user is not None:
        data = organization.objects.filter(company_email__exact=username)
        context = {'orgInfo': data}
        return render(request, 'organization/organizationwelcome.html', context)
    
    else:
        messages.info(request, 'You username or password is incorrect, please try again!')
        return render(request, 'organization/organizationlogin.html')
    

def createJobListing(request):
    try:
        status = request.POST.get('status')
        city = request.POST.get('city')
        job_title = request.POST.get('job_title')
        contracts = request.POST.get('contracts')
        relocation = request.POST.get('relocation')
        description = request.POST.get('description')
        compensation = request.POST.get('compensation')
        organization_int = request.POST.get('orgID')
        organization_int = int(organization_int)
        skillName = request.POST.get('skillname')
        skill_value = request.POST.get('skill_value')   
    
    except Exception:
        print('error')

    listing.objects.create(
        status = status, 
        city = city, 
        job_title = job_title, 
        contracts = contracts,
        relocation = relocation,
        compensation = compensation, 
        description = description,
        organization = organization.objects.get(organization_id__exact = organization_int)     
    )
    
    if (skill.objects.filter(skill_name__iexact = skillname).exists()):
        skillob = skill.objects.get(skill_name__iexact = skillname)

        skill_id = skillob.skill_id 
    
    # PK from the listing object 
    listing_id_FK = listing.listing_id

    listing_skills.objects.create(
        skill_value = skill_value,
        skill_id = skill_id,
        listing_id = listing_id_FK
    )

    data = listing.objects.filter(organization__exact=organization_int)
    context = {'ListingInfo': data}
    return render(request, 'organization/organizationwelcome.html', context)

def companyLogout(request):
    logout(request)
    messages.info(request, "You have logged out successfully!")
    return redirect("index")


def viewApplicant(request, id):
    rec_applicants = []
    print(request.session['username'])
        
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

    context = {
        'rec_users': rec_applicants,
        'applicant': curr_applicant,
        'skill_set': skill_names,
    }
    
    return render(request, 'organization/viewapplicant.html', context)
















# mentor stuff
def mentorAddPageView(request):
    # pass organization id, nothing else should be necessary
    orgID = request.POST['orgID']

    context = {
        'orgID' : orgID
    }

    return render(request, 'organization/addmentor.html', context)

def createMentor(request):
    # create mentor object, reroute to organizationwelcome and pass orgInfo
    orgID = request.POST['orgID']
    fName = request.POST['first-name']
    lName = request.POST['last-name']
    indName = request.POST['industry-name']

    orgObject = organization.objects.get(organization_id=orgID)

    mentor.objects.create(organization=orgObject, first_name=fName, last_name=lName, industry=indName)


    data = organization.objects.filter(company_id__exact=orgID)
    context = {'orgInfo': data}
    return render(request, 'organization/organizationwelcome.html', context)

def viewMentors(request):
    pass


