# Generated by Django 2.1 on 2019-04-23 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0011_auto_20190313_0844'),
        ('library', '0003_auto_20190401_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(max_length=255, verbose_name='Action')),
                ('old', models.CharField(blank=True, max_length=255, verbose_name='Old value')),
                ('new', models.CharField(blank=True, max_length=255, verbose_name='New value')),
                ('gp_practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisations.OrganisationGeneralPractice')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
