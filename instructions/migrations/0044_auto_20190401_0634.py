# Generated by Django 2.1 on 2019-04-01 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0043_auto_20190329_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='invoice_in_week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payment.WeeklyInvoice'),
        ),
    ]