from django.db import models
from organization.models import skill, mentor, organization
from person.models import applicant

# Create your models here.

class offers_review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(organization, on_delete=models.CASCADE)
    compensation = models.DecimalField(max_digits=8, decimal_places=2)
    satisfaction = models.IntegerField()

class message(models.Model):
    message_id = models.IntegerField(primary_key=True)
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(mentor, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    timesent = models.DateTimeField(auto_now=True, auto_now_add=False)
class applicant_skills(models.Model):
    applicant_id = models.ForeignKey(applicant, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(skill, on_delete=models.CASCADE)