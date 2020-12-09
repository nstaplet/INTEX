from django.urls import path
from .views import indexPageView
from .views import applicantloginPageView
from .views import applicantsignupPage, applicantLogin, applicant_dash, createApplicant, offersPageView, updateSkills, updateSkillsPageView, messagesPageView, singleMessageView, createMessage, applicantLogout, viewlisting, applicantwelcome


urlpatterns = [
    path('', indexPageView, name='index'),
    path('applicantlogin/', applicantloginPageView, name='applicantlogin'),
    path('applicantsignup/', applicantsignupPage, name='applicantsignup'),
    path('applicantwelcome/', applicantLogin, name='applicantLogin'),
    path('applicanthome', applicantwelcome, name='applicantwelcome'),
    path('dashboard/', applicant_dash, name='dashboard'),
    path('createapplicant', createApplicant, name='createApplicant'),
    path('viewlisting/<int:org_id>/<int:list_id>', viewlisting, name='viewlisting'),
    path('applicantoffers/', offersPageView, name='applicantoffers'),
    path('updateskills', updateSkills, name='updateskills'),
    path('updateskillspage/', updateSkillsPageView, name='updateskillspage'),
    path('messages/', messagesPageView, name='messagespageview'),
    path('message/', singleMessageView, name='singlemessageview'),
    path('createmessage', createMessage, name='createmessage'),
    path('applicantLogout', applicantLogout, name='applicantLogout')
]