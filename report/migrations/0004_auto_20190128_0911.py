# Generated by Django 2.1 on 2019-01-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20190122_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientreportauth',
            old_name='patient_count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='patientreportauth',
            old_name='patient_locked_report',
            new_name='locked_report',
        ),
        migrations.RenameField(
            model_name='patientreportauth',
            old_name='patient_mobi_request_id',
            new_name='mobi_request_id',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_count',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_locked_report',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_mobi_request_id',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_mobi_request_voice_id',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_verify_sms_pin',
        ),
        migrations.RemoveField(
            model_name='patientreportauth',
            name='third_party_verify_voice_pin',
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='expired_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='locked_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='mobi_request_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='mobi_request_voice_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='verify_sms_pin',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='verify_voice_pin',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.RemoveField(
            model_name='thirdpartyauthorisation',
            name='expired',
        ),
        migrations.AddField(
            model_name='thirdpartyauthorisation',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
