from django.contrib import admin
from .models import organization, mentor, offers_made, skill, listing_skills, listing

# Register your models here.
admin.site.register(organization)
admin.site.register(mentor)
admin.site.register(offers_made)
admin.site.register(skill)
admin.site.register(listing_skills)
admin.site.register(listing)