# Generated by Django 2.1 on 2019-03-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0029_auto_20190222_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='download_attachments',
            field=models.TextField(blank=True),
        ),
    ]