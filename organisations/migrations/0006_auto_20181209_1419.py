# Generated by Django 2.1 on 2018-12-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0005_auto_20181127_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationgeneralpractice',
            name='onboarding_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='organisationgeneralpractice',
            name='onboarding_job_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
