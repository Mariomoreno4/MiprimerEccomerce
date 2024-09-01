# Generated by Django 4.2.7 on 2023-11-16 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0023_prestamos_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to='imagenes_perfil/')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
