# Generated by Django 4.2.5 on 2023-10-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0014_auto_20210707_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10)),
                ('puesto', models.CharField(max_length=10)),
                ('sueldo', models.IntegerField()),
            ],
        ),
    ]
