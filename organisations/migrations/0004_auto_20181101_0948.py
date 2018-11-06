# Generated by Django 2.1 on 2018-11-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0003_organisationgeneralpractice_accept_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisationgeneralpractice',
            name='payment_bank_account_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationgeneralpractice',
            name='payment_bank_holder_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='organisationgeneralpractice',
            name='payment_bank_sort_code',
            field=models.CharField(blank=True, max_length=255),
        )

    ]
