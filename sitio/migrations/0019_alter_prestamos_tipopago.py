# Generated by Django 4.2.5 on 2023-10-19 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0018_remove_prestamos_carrito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='TipoPago',
            field=models.CharField(max_length=90),
        ),
    ]
