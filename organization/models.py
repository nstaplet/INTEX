from django.db import models
# Need to wait for the applicant app models 
from person.models import applicant

# Create your models here.
class organization(models.Model):
    organization_id = models.IntegerField(primary_key=True),
    company_name = models.CharField(max_length=30),
    company_email = models.CharField(max_length=70),
    company_address = models.CharField(max_length=30),
    size = models.CharField(max_length=10),
    sectors = models.CharField(max_length=10)

class mentor(models.Model):
    mentor_id = models.IntegerField(primary_key=True),
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE),
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length=30),
    industry = models.CharField(max_length=20)

class offers_made(models.Model):
    offer_id = models.IntegerField(primary_key=True),
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE),
    status = models.CharField(max_length=30),
    city = models.CharField(max_length=30),
    job_title = models.CharField(max_length=70),
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE),
    contracts = models.CharField(max_length=30),
    matching_skills = models.IntegerField()

class skill(models.Model):
    skill_id = models.IntegerField(primary_key=True),
    skill_name = models.CharField(max_length=50)

class listing_skills(models.Model):
    listing_id = models.IntegerField(primary_key=True),
    skill_id = models.IntegerField(),
    skill_value = models.IntegerField()

class listing(models.Model):
    listing_id = models.IntegerField(primary_key=True),
    status = models.CharField(max_length=30),
    city = models.CharField(max_length=30),
    job_title = models.CharField(max_length=70),
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE),
    contracts = models.CharField(max_length=30),
    total_skills = models.IntegerField(),
    compensation = models.DecimalField(max_digits=7, decimal_places=2, null= True),
    relocation = models.BooleanField(default=False)
