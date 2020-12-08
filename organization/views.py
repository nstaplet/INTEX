from django.shortcuts import render
from django.http import HttpResponse

# models
from django.contrib.auth import authenticate, login
from .models import organization, skill, listing, listing_skills, mentor, offers_made
from django.contrib import messages
from django.contrib.auth.models import User

# outside functions
from .algorithms import recommend_users

def organizationWelcomePageView(request) :

    #username = request.POST['username']
    #password = request.POST['password']

    #user = authenticate(username = username, password = password)

    #if user is not None:
    return render(request, 'organization/organizationwelcome.html')

    #else:
    #    return render(request, 'organization/organizationlogin.html')

def organizationlogin(request) :
    return render(request, 'organization/organizationlogin.html')

def organizationsignup(request) :
    return render(request, 'organization/organizationsignup.html')

def createOrganization(request):
    company_name = request.POST['company_name']
    company_email = request.POST['company_email']
    company_password = request.POST['company_password']
    company_address = request.POST['company_address']
    size = request.POST['company_size']
    sectors = request.POST['company_sector']
<<<<<<< HEAD
    # if request.method == 'POST':
    # new_company = organization()

    # new_company.company_name = request.POST.get['company_name']
    # new_company.company_email = request.POST.get['company_email']
    # new_company.company_address = request.POST.get['company_address']
    # new_company.company_password = request.POST.get['company_password']
    # new_company.size = request.POST.get['company_size']
    # new_company.sectors = request.POST.get['company_sector']

    # new_company.save() <- !!! I think this was supposed to be commented out. It's technically an undefined variable

=======
    
>>>>>>> 9e8adc5d521cc4dab919208ee97fa869922280d9
    if (organization.objects.filter(company_name__exact=company_name).exists()):
        messages.info(request, 'That company name has already been claimed. Please try again.')
        return render(request, 'organization/organizationsignup.html')


    elif (organization.objects.filter(company_email__exact=company_email).exists()):
        messages.info(request, 'That company email has already been claimed. Please try again.')
        return render(request, 'organization/organizationsignup.html')

    else:
        organization.objects.create(company_name = company_name, company_email = company_email, company_address = company_address, size=size, sectors = sectors)
<<<<<<< HEAD
        User.objects.create_user(company_email=company_email, company_password = company_password)
=======
        User.objects.create_user(username=company_email, password = company_password)
        data = organization.objects.filter(company_email__exact=company_email)
        context = {'orgInfo': data}
        return render(request, 'organization/organizationwelcome.html', context)
    # if request.method == 'POST':
    # new_company = organization()

    # new_company.company_name = request.POST.get['company_name']
    # new_company.company_email = request.POST.get['company_email']
    # new_company.company_address = request.POST.get['company_address']
    # new_company.company_password = request.POST.get['company_password']
    # new_company.size = request.POST.get['company_size']
    # new_company.sectors = request.POST.get['company_sector']
>>>>>>> 9e8adc5d521cc4dab919208ee97fa869922280d9
    
    # new_company.save()

def companyLogin(request):
    username = request.POST['company_email']
    password = request.POST['company_password']

    user = authenticate(username = username, password = password)

    if user is not None:
        data = organization.objects.filter(company_email__exact=username)
        context = {'orgInfo': data}
        return render(request, 'organization/organizationwelcome.html', context)
    
    else:
        return render(request, 'organization/organizationlogin.html')
    
def createJobListing(request):
    status = request.POST['status']
    city = request.POST['city']
    job_title = request.POST['job_title']
    contracts = request.POST['contracts']
    relocation = request.POST['relocation']
    description = request.POST['description']
    compensation = request.POST['compensation']
    organization_int = request.POST['orgID']
    organization_int = int(organization_int)


    if (listing.objects.filter(job_title__exact=job_title).exists()):
        messages.info(request, 'You have already posted a listing with job title ' + job_title + '.')
        return render(request,'organization/organizationwelcome.html')
    
    else:
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

        data = listing.objects.filter(organization__exact=organization_int)
        context = {'ListingInfo': data}
        return render(request, 'organization/organizationwelcome.html', context)

