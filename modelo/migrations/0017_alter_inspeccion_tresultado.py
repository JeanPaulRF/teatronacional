# Generated by Django 4.1.1 on 2022-10-16 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0016_alter_area_imagen2_alter_area_imagen3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspeccion',
            name='tResultado',
            field=models.CharField(choices=[('CONSERVACION', 'CONSERVACION'), ('RESTAURACION', 'RESTAURACION'), ('SIN_DEFINIR', 'SIN_DEFINIR')], max_length=25),
        ),
    ]
