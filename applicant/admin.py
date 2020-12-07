from django.contrib import admin
from .models import message, applicant_skills, offers_review

# Register your models here.
admin.site.register(message)
admin.site.register(applicant_skills)
admin.site.register(offers_review)