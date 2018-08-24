# Generated by Django 2.1 on 2018-08-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0002_auto_20180822_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='NHSgpPractice',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('reference', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('address_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('address_line3', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'NHS GP Practice',
            },
        ),
        migrations.AlterField(
            model_name='organisationbase',
            name='contact_telephone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationbase',
            name='fax_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationbase',
            name='generic_telephone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]