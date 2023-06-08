# Generated by Django 4.2.1 on 2023-06-06 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("db_group", models.CharField(max_length=50, null=True)),
                ("code", models.CharField(max_length=50, null=True)),
                ("category", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "serving_amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="serving_amount",
                    ),
                ),
                ("serving_unit", models.CharField(max_length=50)),
                (
                    "energy",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="energy(kcal)",
                    ),
                ),
                (
                    "protein",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="protein(g)"
                    ),
                ),
                (
                    "carbohydrate",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="carbohydrate(g)",
                    ),
                ),
                (
                    "sugar",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="sugar(g)",
                    ),
                ),
                (
                    "sodium",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        null=True,
                        verbose_name="sodium(mg)",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="food.manufacturer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]