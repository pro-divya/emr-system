# Generated by Django 2.1 on 2019-06-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_merge_20190405_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyinvoice',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Printed', 'Printed')], default='Draft', max_length=7),
        ),
    ]
