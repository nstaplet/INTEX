from django.urls import path
from .views import organizationWelcomePageView
from .views import organizationlogin
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, mentorAddPageView, createMentor
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, viewApplicant
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, mentorAddPageView

urlpatterns = [
    path('organizationwelcome/', organizationWelcomePageView, name='organizationwelcome'),
    # Added for creat new listing
    path('organizationwelcome', createJobListing, name='createJobListing'),
    path('organizationlogin/', organizationlogin, name='organizationlogin'),
    path('organizationsignup/', organizationsignup, name='organizationsignup'),
    path('createOrganization/', createOrganization, name='createOrganization'),
    path('companyLogin/', companyLogin, name='companyLogin'),
    path('companyLogout/', companyLogout, name='companyLogout'),
    path('viewapplicant/<int:id>', viewApplicant, name='viewapplicant'), 
    path('mentorAdd/', mentorAddPageView, name='mentoraddpageview'),
    path('mentorCreate', createMentor, name='creatementor')
]
