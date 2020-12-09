from django.db import models
from person.models import applicant

# Create your models here.
class organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=30, blank=True)
    company_email = models.CharField(max_length=70, blank=True)
    company_address = models.CharField(max_length=70, blank=True)
    size = models.CharField(max_length=10, blank=True)
    sectors = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return (f'{self.company_name}')

class mentor(models.Model):
    mentor_id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    industry = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')

class offers_made(models.Model):
    offer_id = models.IntegerField(primary_key=True)
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    contracts = models.CharField(max_length=30, blank=True)
    matching_skills = models.IntegerField()

    def __str__(self):
        return (f'{self.job_title}')

class skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return (f'{self.skill_name}')

class listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    job_title = models.CharField(max_length=70, blank=True)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    contracts = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    total_skills = models.IntegerField(default=0)
    compensation = models.DecimalField(max_digits=7, decimal_places=2, null= True, blank=True, default=0)
    relocation = models.BooleanField(default=False)

    def __str__(self):
        return (f'{self.job_title} {self.compensation}')

    # @property
    # def re_listingID(self):
    #     return self.listing_id

class listing_skills(models.Model):
    skill_listing_id = models.AutoField(primary_key=True)
    skill_id = models.ForeignKey(skill, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(listing, on_delete=models.CASCADE)
    skill_value = models.IntegerField(default=0)

    def __str__(self):
        return (f'{self.skill_id}')