from django.urls import path
from .views import organizationWelcomPageView

urlpatterns = [
    path('organization/', organizationWelcomPageView, name='orgwelcome')
]
