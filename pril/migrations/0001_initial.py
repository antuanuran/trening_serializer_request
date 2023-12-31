# Generated by Django 4.2.5 on 2023-11-02 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pass",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "1. Заглушка",
                "verbose_name_plural": "1. Заглушки",
            },
        ),
        migrations.CreateModel(
            name="Item",
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
                ("title", models.CharField(max_length=50)),
                ("proverka", models.CharField(max_length=50)),
                (
                    "pass_fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="pril.pass",
                    ),
                ),
            ],
            options={
                "verbose_name": "2. Item",
                "verbose_name_plural": "2. Items",
            },
        ),
    ]
