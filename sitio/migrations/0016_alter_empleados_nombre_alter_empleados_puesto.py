# Generated by Django 4.2.5 on 2023-10-19 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0015_empleados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='puesto',
            field=models.CharField(max_length=50),
        ),
    ]
