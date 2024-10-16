# Generated by Django 5.1.2 on 2024-10-16 20:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0015_delete_solicitudretiro'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudRetiro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cant_residuos', models.IntegerField()),
                ('tipo_residuo', models.CharField(max_length=14)),
                ('direccion', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=400)),
                ('destino_final', models.CharField(max_length=100)),
                ('ruta_optima', models.CharField(max_length=300)),
                ('valor', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]