from django.db import models

# Create your models here.
class applicant(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email_opt_in = models.BooleanField(default=True)
    city = models.CharField(max_length=25)