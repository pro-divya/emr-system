# Generated by Django 2.1 on 2019-06-27 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0055_auto_20190619_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='patient_notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instruction',
            name='third_party_notification',
            field=models.BooleanField(default=False),
        ),
    ]
