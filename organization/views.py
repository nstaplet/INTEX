from django.shortcuts import render
from django.http import HttpResponse

# models
from django.contrib.auth import authenticate, login
from .models import organization, skill, listing, listing_skills, mentor, offers_made
from django.contrib import messages

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
    # if request.method == 'POST':
    # new_company = organization()

    # new_company.company_name = request.POST.get['company_name']
    # new_company.company_email = request.POST.get['company_email']
    # new_company.company_address = request.POST.get['company_address']
    # new_company.company_password = request.POST.get['company_password']
    # new_company.size = request.POST.get['company_size']
    # new_company.sectors = request.POST.get['company_sector']
    
    new_company.save()


    if (organization.objects.filter(company_name__exact=company_name).exists()):
        messages.info(request, 'That company name has already been claimed. Please try again.')
    
        return render(request, 'organization/organizationsignup.html')


    elif (organization.objects.filter(company_email__exact=company_email).exists()):
        messages.info(request, 'That company email has already been claimed. Please try again.')
    
        return render(request, 'organization/organizationsignup.html')

    else:
        organization.objects.create(company_name = company_name, company_email = company_email, company_address = company_address, size=size, sectors = sectors)
    User.objects.create_user(company_email=company_email, company_password = company_password)
    
    return render(request, 'organization/organizationwelcome.html')

def companyLogin(request):
    username = request.POST['company_email']
    password = request.POST['company_password']

    user = authenticate(username = username, password = password)

    if user is not None:
        data = organization.objects.filter(company_email__exact=username)
        return render(request, 'organization/organizationwelcome.html')
    
    else:
        return render(request, 'organization/organizationlogin.html')
