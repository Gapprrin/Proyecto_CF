# Generated by Django 5.1.2 on 2024-10-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0009_delete_solicitudretiro'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudRetiro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]