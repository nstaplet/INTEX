from django.urls import path
from .views import organizationWelcomePageView
from .views import organizationlogin
from .views import organizationsignup, createOrganization, companyLogin, createJobListing, companyLogout, mentorAddPageView, createMentor, viewApplicant, viewMentors, viewMessages, mentorCreateMessage, mentorSingleMessageView

urlpatterns = [
    # path('go_create_skills/', go_create_skills, name='go_create_skills'),
    path('organizationwelcome', organizationWelcomePageView, name='organizationwelcome'),
    path('createlisting', createJobListing, name='createJobListing'),
    path('organizationlogin/', organizationlogin, name='organizationlogin'),
    path('organizationsignup/', organizationsignup, name='organizationsignup'),
    path('createOrganization/', createOrganization, name='createOrganization'),
    path('companyLogin/', companyLogin, name='companyLogin'),
    path('companyLogout/', companyLogout, name='companyLogout'),
    path('viewapplicant/<int:id>', viewApplicant, name='viewapplicant'), 
    path('mentorAdd/', mentorAddPageView, name='mentoraddpageview'),
    path('mentorCreate', createMentor, name='creatementor'),
    path('currentMentors/', viewMentors, name='viewmentors'),
    path('viewmessages', viewMessages, name='viewmessages'),
    path('createmessage', mentorCreateMessage, name='mentorcreatemessage'),
    path('mentorsinglemessageview', mentorSingleMessageView, name='mentorsinglemessageview')
]
