# Generated by Django 2.1 on 2019-03-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='key',
            field=models.CharField(max_length=255, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='library',
            name='value',
            field=models.CharField(blank=True, max_length=255, verbose_name='Replaced by'),
        ),
    ]
