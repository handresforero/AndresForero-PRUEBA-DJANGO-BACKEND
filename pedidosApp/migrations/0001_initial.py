# Generated by Django 4.2.1 on 2023-05-10 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("conductoresApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        max_length=6, primary_key=True, serialize=False
                    ),
                ),
                ("tipo_pedido", models.CharField(max_length=20, verbose_name="Tipo")),
                (
                    "direccion",
                    models.CharField(max_length=50, verbose_name="Direccion"),
                ),
                (
                    "conductor_id_2",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="conductor_id",
                        to="conductoresApp.conductor",
                    ),
                ),
            ],
        ),
    ]
