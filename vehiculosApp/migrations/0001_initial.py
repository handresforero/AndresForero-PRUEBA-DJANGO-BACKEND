# Generated by Django 4.2.1 on 2023-05-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vehiculo",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("modelo", models.CharField(max_length=4, verbose_name="Modelo")),
                (
                    "placa",
                    models.CharField(max_length=7, unique=True, verbose_name="Placa"),
                ),
                (
                    "capacidad",
                    models.CharField(max_length=7, null=True, verbose_name="Capacidad"),
                ),
            ],
        ),
    ]
