# Generated by Django 2.1 on 2018-12-26 05:34

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    """
        Convert all instruction.gp_earns, instruction.medi_earns from None to 0 that has already existed in the database
    """
    Instruction = apps.get_model('instructions', 'Instruction')
    db_alias = schema_editor.connection.alias
    exist_instructions = Instruction.objects.using(db_alias).all()
    for instruction in exist_instructions:
        if instruction.gp_earns is None:
            instruction.gp_earns = 0
        if instruction.medi_earns is None:
            instruction.medi_earns = 0
        instruction.save()


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0015_auto_20181226_0425'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AlterField(
            model_name='instruction',
            name='gp_earns',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='instruction',
            name='medi_earns',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
