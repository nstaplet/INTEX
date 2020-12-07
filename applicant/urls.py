from django.urls import path
from .views import indexPageView
from .views import applicantloginPage
from .views import applicantsignupPage, applicantwelcome, applicant_dash, createApplicant, offersPageView


urlpatterns = [
    path('', indexPageView, name='index'),
    path('applicantlogin/', applicantloginPage, name='applicantlogin'),
    path('applicantsignup/', applicantsignupPage, name='applicantsignup'),
    path('applicantwelcome/', applicantwelcome, name='applicantwelcome'),
    path('dashboard', applicant_dash, name='dashboard'),
    path('createapplicant', createApplicant, name='createApplicant'),
    path('applicantoffers', offersPageView, name='applicantoffers'),
]