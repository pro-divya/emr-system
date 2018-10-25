# Generated by Django 2.1 on 2018-10-22 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicalreport', '0003_amendmentsforrecord_instruction_checked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='acute_prescription_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='attachment_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='bloods_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='comment_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='consultation_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='instruction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructions.Instruction'),
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='patient_emis_number',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='referral_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='repeat_prescription_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amendmentsforrecord',
            name='significant_problem_notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
