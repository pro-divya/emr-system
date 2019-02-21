# Generated by Django 2.1.5 on 2019-02-05 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0023_instruction_medical_xml_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instruction',
            options={'ordering': ('-created',), 'permissions': (('create_sars', 'Create SARS'), ('reject_amra', 'Reject AMRA'), ('reject_sars', 'Reject SARS'), ('process_amra', 'Process AMRA'), ('process_sars', 'Process SARS'), ('allocate_gp', 'Allocate to other user to process'), ('sign_off_amra', 'Sign off AMRA'), ('sign_off_sars', 'Sign off SARS'), ('view_completed_amra', 'View completed AMRA'), ('view_completed_sars', 'View completed SARS'), ('view_summry_report', 'View summary report')), 'verbose_name': 'Instruction'},
        ),
    ]