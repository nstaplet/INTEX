from django.urls import path
from .views import organizationWelcomePageView
from .views import organizationlogin
from .views import organizationsignup, createOrganization, companyLogin, createJobListing

urlpatterns = [
    path('organizationwelcome/', organizationWelcomePageView, name='organizationwelcome'),
    # Added for creat new listing
    path('organizationwelcome', createJobListing, name='createJobListing'),

    path('organizationlogin/', organizationlogin, name='organizationlogin'),
    path('organizationsignup/', organizationsignup, name='organizationsignup'),
    path('createOrganization/', createOrganization, name='createOrganization'),
    path('companyLogin/', companyLogin, name='companyLogin'),
    
]
