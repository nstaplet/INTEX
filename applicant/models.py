from django.db import models
from organization.models import skill, mentor, organization
from person.models import applicant

# Create your models here.

class offers_review(models.Model):
    review_id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE)
    organization = models.ForeignKey(organization, on_delete=models.CASCADE)
    compensation = models.DecimalField(max_digits=8, decimal_places=2)
    satisfaction = models.IntegerField()

class message(models.Model):
    message_id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE)
    mentor = models.ForeignKey(mentor, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    timesent = models.DateTimeField(auto_now=True, auto_now_add=False)
    sender_applicant = models.BooleanField(default=True)

class applicant_skills(models.Model):
    id = models.AutoField(primary_key=True)
    applicant = models.ForeignKey(applicant, on_delete=models.CASCADE)
    skill = models.ForeignKey(skill, on_delete=models.CASCADE)