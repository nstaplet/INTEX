# Generated by Django 3.1.2 on 2020-12-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender_applicant',
            field=models.BooleanField(default=True),
        ),
    ]