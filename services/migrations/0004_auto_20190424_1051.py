# Generated by Django 2.1 on 2019-04-24 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_site_control_access'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='site_control_access',
            new_name='SiteAccessControl',
        ),
    ]