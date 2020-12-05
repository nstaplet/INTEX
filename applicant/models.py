from django.db import models
from organization.models import skill, mentor, organization

# Create your models here.
class applicant(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_opt_in = models.BooleanField(default=True)
    city = models.CharField(max_length=25)
    skills = models.ManyToManyField("organization.skill")

class offers_review(models.Model):
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE)
    compensation = models.DecimalField(max_digits=8, decimal_places=2)
    satisfaction = models.IntegerField()

class message(models.Model):
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(mentor, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    timesent = models.DateTimeField(auto_now=True, auto_now_add=False)

# unused composite linking table
# class applicant_skills(models.Model):
    # applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    # skill_id = models.ForeignKey(skill, on_delete=models.CASCADE)