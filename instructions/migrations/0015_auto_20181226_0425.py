# Generated by Django 2.1 on 2018-12-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0014_auto_20181224_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='initial_monetary_value',
        ),
        migrations.AddField(
            model_name='instruction',
            name='gp_earns',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='medi_earns',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
