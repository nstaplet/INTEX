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
    if request.method == 'POST':
        new_company = organization()

        new_company.company_name = request.POST.get['company_name']
        new_company.company_email = request.POST.get['company_email']
        new_company.company_address = request.POST.get['company_address']
        # company_password = request.POST['password']
        new_company.size = request.POST.get['company_size']
        new_company.sectors = request.POST.get['company_sector']
        
        new_company.save()


        if (organization.objects.filter(company_name__exact=new_company.company_name).exists()):
            messages.info(request, 'That company name has already been claimed. Please try again.')
        
            return render(request, 'organization/organizationsignup.html')


        elif (organization.objects.filter(company_email__exact=new_company.company_email).exists()):
            messages.info(request, 'That company email has already been claimed. Please try again.')
        
            return render(request, 'organization/organizationsignup.html')

        # else:
        #     applicant.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, city=city, email_opt_in=email_opt_in)
        #     User.objects.create_user(username=username, email=email, password=password)

    return render(request, 'applicant/organizationwelcome.html')