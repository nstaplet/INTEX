# Generated by Django 3.1.2 on 2020-12-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20201205_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='company_address',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterUniqueTogether(
            name='listing_skills',
            unique_together=set(),
        ),
    ]
