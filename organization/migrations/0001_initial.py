# Generated by Django 3.1.3 on 2020-12-07 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listing_skills',
            fields=[
                ('skill_listing_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('skill_id', models.IntegerField(default=0)),
                ('listing_id', models.IntegerField(default=0)),
                ('skill_value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('organization_id', models.IntegerField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=30)),
                ('company_email', models.CharField(blank=True, max_length=70)),
                ('company_address', models.CharField(blank=True, max_length=70)),
                ('size', models.CharField(blank=True, max_length=10)),
                ('sectors', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('skill_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('skill_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='offers_made',
            fields=[
                ('offer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('job_title', models.CharField(blank=True, max_length=70)),
                ('contracts', models.CharField(blank=True, max_length=30)),
                ('matching_skills', models.IntegerField()),
                ('applicant', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='person.applicant')),
                ('organization', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('mentor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('industry', models.CharField(blank=True, max_length=20)),
                ('organization', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='listing',
            fields=[
                ('listing_id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('job_title', models.CharField(blank=True, max_length=70)),
                ('contracts', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('total_skills', models.IntegerField(default=0)),
                ('compensation', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True)),
                ('relocation', models.BooleanField(default=False)),
                ('organization', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
    ]
