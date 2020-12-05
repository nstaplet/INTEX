from django.urls import path
from .views import organizationWelcomePageView
from .views import organizationlogin
from .views import organizationsignup

urlpatterns = [
    path('organization/', organizationWelcomePageView, name='organizationwelcome'),
    path('organizationlogin/', organizationlogin, name='organizationlogin'),
    path('organizationsignup/', organizationsignup, name='organizationsignup'),
]
