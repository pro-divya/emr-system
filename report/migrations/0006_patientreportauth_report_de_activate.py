# Generated by Django 2.1.5 on 2019-02-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_auto_20190130_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientreportauth',
            name='report_de_activate',
            field=models.BooleanField(default=False, verbose_name='Deactivated at patient request'),
        ),
    ]
