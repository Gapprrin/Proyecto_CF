# Generated by Django 5.1.2 on 2024-10-16 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudretiro',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='solicitudretiro',
            name='ruta',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
