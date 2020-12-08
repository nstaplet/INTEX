from django.shortcuts import render, redirect
from django.http import HttpResponse

# models
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from .models import organization, skill, listing, listing_skills, mentor, offers_made
from django.contrib import messages
from django.contrib.auth.models import User

# outside functions
# from .algorithms import recommend_users

def organizationWelcomePageView(request) :
    return render(request, 'organization/organizationwelcome.html')

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
    username = request.POST['company_email']
    password = request.POST['company_password']

    user = authenticate(username = username, password = password)

    if user is not None:
        data = organization.objects.filter(company_email__exact=username)
        context = {'orgInfo': data}
        return render(request, 'organization/organizationwelcome.html', context)
    
    else:
        messages.info(request, 'You username or password is incorrect, please try again!')
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

def companyLogout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index")