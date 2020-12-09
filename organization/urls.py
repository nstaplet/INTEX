from django.urls import path
from .views import organizationWelcomePageView
from .views import organizationlogin
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, create_skills, go_create_skills
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, mentorAddPageView, createMentor, viewApplicant, viewMentors, viewMessages

urlpatterns = [
    path('organizationwelcome', organizationWelcomePageView, name='organizationwelcome'),
    # Added for creat new listing
    path('createlisting', createJobListing, name='createJobListing'),
    path('organizationlogin/', organizationlogin, name='organizationlogin'),
    path('organizationsignup/', organizationsignup, name='organizationsignup'),
    path('createOrganization/', createOrganization, name='createOrganization'),
    path('companyLogin/', companyLogin, name='companyLogin'),
    path('companyLogout/', companyLogout, name='companyLogout'),
    path('create_skills/', create_skills, name='create_skills'),
    path('go_create_skills/', go_create_skills, name='go_create_skills'),
    path('viewapplicant/<int:id>', viewApplicant, name='viewapplicant'), 
    path('mentorAdd/', mentorAddPageView, name='mentoraddpageview'),
    path('mentorCreate', createMentor, name='creatementor'),
    path('currentMentors/', viewMentors, name='viewmentors'),
    path('viewmessages', viewMessages, name='viewmessages'),
]
