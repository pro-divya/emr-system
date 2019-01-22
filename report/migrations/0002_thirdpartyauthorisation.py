# Generated by Django 2.1 on 2019-01-22 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdPartyAuthorisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('case_reference', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('family_phone_number', models.CharField(max_length=20)),
                ('office_phone_number', models.CharField(max_length=20)),
                ('expired', models.DateField(null=True)),
                ('patient_report_auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_parties', to='report.PatientReportAuth')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
