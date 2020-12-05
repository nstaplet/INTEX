from django.urls import path
from .views import indexPageView
from .views import applicantlogin
from .views import applicantsignup, applicantwelcome


urlpatterns = [
    path('', indexPageView, name='index'),
    path('applicantlogin', applicantlogin, name='applicantlogin'),
    path('applicantsignup', applicantsignup, name='applicantsignup'),
    path('applicantwelcome', applicantwelcome, name='applicantwelcome')
]