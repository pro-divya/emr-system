# Generated by Django 2.1 on 2018-11-09 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisations', '0001_initial'),
        ('snomedct', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateConditionsOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snomedct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snomedct.SnomedConcept')),
            ],
            options={
                'verbose_name': 'Template Conditions Of Interest',
            },
        ),
        migrations.CreateModel(
            name='TemplateInstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('template_title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('AMRA', 'AMRA'), ('SARS', 'SARS')], max_length=4)),
                ('client_organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organisations.OrganisationClient')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Template of Instruction',
            },
        ),
        migrations.CreateModel(
            name='TemplateInstructionAdditionalQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('response_mandatory', models.BooleanField(default=False)),
                ('answer_format', models.CharField(choices=[('NUM', 'Number'), ('TXT', 'Text')], max_length=3)),
                ('template_instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.TemplateInstruction')),
            ],
            options={
                'verbose_name': 'Template Instruction Additional Question',
            },
        ),
        migrations.AddField(
            model_name='templateconditionsofinterest',
            name='template_instruction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.TemplateInstruction'),
        ),
    ]
