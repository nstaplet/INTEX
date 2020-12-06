# Generated by Django 3.1.2 on 2020-12-06 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offers_review',
            fields=[
                ('review_id', models.IntegerField(primary_key=True, serialize=False)),
                ('compensation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('satisfaction', models.IntegerField()),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.applicant')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('message_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=300)),
                ('timesent', models.DateTimeField(auto_now=True)),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.applicant')),
                ('mentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.mentor')),
            ],
        ),
        migrations.CreateModel(
            name='applicant_skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.applicant')),
                ('skill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.skill')),
            ],
        ),
    ]
