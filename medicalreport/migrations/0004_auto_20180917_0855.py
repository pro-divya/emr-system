# Generated by Django 2.1 on 2018-09-17 07:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalreport', '0003_redaction_patient_emis_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redaction',
            name='acute_prescription_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='attachment_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='bloods_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='consultation_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='redacted_xpaths',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='referral_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='repeat_prescription_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='redaction',
            name='significant_problem_notes',
            field=models.TextField(null=True),
        ),
    ]