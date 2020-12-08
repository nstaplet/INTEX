# Generated by Django 3.1.2 on 2020-12-08 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listing_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='listing_skills',
            name='listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.listing'),
        ),
        migrations.AlterField(
            model_name='listing_skills',
            name='skill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.skill'),
        ),
        migrations.AlterField(
            model_name='listing_skills',
            name='skill_listing_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='mentor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='offers_made',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.applicant'),
        ),
        migrations.AlterField(
            model_name='offers_made',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
