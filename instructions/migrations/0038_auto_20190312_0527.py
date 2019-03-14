# Generated by Django 2.1 on 2019-03-12 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0037_merge_20190311_0652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instruction',
            options={'ordering': ('-created',), 'permissions': (('create_sars', 'Create SARS'), ('reject_amra', 'Reject AMRA'), ('reject_sars', 'Reject SARS'), ('process_amra', 'Process AMRA'), ('process_sars', 'Process SARS'), ('allocate_gp', 'Allocate to other user to process'), ('sign_off_amra', 'Sign off AMRA'), ('sign_off_sars', 'Sign off SARS'), ('view_completed_amra', 'View completed AMRA'), ('view_completed_sars', 'View completed SARS'), ('view_summary_report', 'View summary report'), ('view_account_pages', 'view account page'), ('authorise_fee', 'Authorise Fee'), ('amend_fee', 'Amend Fee')), 'verbose_name': 'Instruction'},
        ),
    ]