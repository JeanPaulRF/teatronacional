# Generated by Django 4.1.1 on 2022-10-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0012_alter_area_imagen1_alter_elemento_imagen1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='imagen1',
            field=models.ImageField(default='teatrologo.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='imagen1',
            field=models.ImageField(default='teatrologo.jpg', upload_to=''),
        ),
    ]
