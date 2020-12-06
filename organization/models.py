from django.db import models
from person.models import applicant

# Create your models here.
class organization(models.Model):
    organization_id = models.IntegerField(primary_key=True ,default=0)
    company_name = models.CharField(max_length=30, blank=True)
    company_email = models.CharField(max_length=70, blank=True)
    company_address = models.CharField(max_length=70, blank=True)
    size = models.CharField(max_length=10, blank=True)
    sectors = models.CharField(max_length=10, blank=True)

class mentor(models.Model):
    mentor_id = models.IntegerField(primary_key=True, default=0)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    industry = models.CharField(max_length=20, blank=True)

class offers_made(models.Model):
    offer_id = models.IntegerField(primary_key=True, default=0)
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    contracts = models.CharField(max_length=30, blank=True)
    matching_skills = models.IntegerField()

class skill(models.Model):
    skill_id = models.IntegerField(primary_key=True, default=0)
    skill_name = models.CharField(max_length=50, blank=True)

class listing_skills(models.Model):
    skill_listing_id = models.IntegerField(primary_key=True, default=0)
    skill_id = models.IntegerField(default=0)
    listing_id = models.IntegerField(default=0)
    skill_value = models.IntegerField(default=0)

class listing(models.Model):
    listing_id = models.IntegerField(primary_key=True, default=0)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    contracts = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    total_skills = models.IntegerField(default=0)
    compensation = models.DecimalField(max_digits=7, decimal_places=2, null= True, default=0)
    relocation = models.BooleanField(default=False)
