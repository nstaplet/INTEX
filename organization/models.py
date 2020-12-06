from django.db import models
from person.models import applicant

# Create your models here.
class organization(models.Model):
    organization_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=30, blank=True)
    company_email = models.CharField(max_length=70, blank=True)
    company_address = models.CharField(max_length=70, blank=True)
    size = models.CharField(max_length=10, blank=True)
    sectors = models.CharField(max_length=10, blank=True)

class mentor(models.Model):
    mentor_id = models.IntegerField(primary_key=True)
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    industry = models.CharField(max_length=20, blank=True)

class offers_made(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    contracts = models.CharField(max_length=30, blank=True)
    matching_skills = models.IntegerField()

class skill(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=50, blank=True)

class listing_skills(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    skill_id = models.IntegerField(default=0)
    skill_value = models.IntegerField(default=0)

class listing(models.Model):
    listing_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE, default=0)
    contracts = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    total_skills = models.IntegerField(default=0)
    compensation = models.DecimalField(max_digits=7, decimal_places=2, null= True, default=0)
    relocation = models.BooleanField(default=False)
