# Generated by Django 4.1.1 on 2022-10-16 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0008_rename_deterio_inspeccion_deterioro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='imagen1',
            field=models.ImageField(default='images/teatrologo.jpg', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='imagen1',
            field=models.ImageField(default='images/teatrologo.jpg', upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
