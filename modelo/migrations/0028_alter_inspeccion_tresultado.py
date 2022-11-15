# Generated by Django 4.1.2 on 2022-11-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0027_alter_inspeccion_tresultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='tResultado',
            field=models.CharField(choices=[('CONSERVACION', 'CONSERVACION'), ('RESTAURACION', 'RESTAURACION'), ('POR_DEFINIR', 'POR_DEFINIR')], default='POR_DEFINIR', max_length=25),
        ),
    ]