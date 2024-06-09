# Generated by Django 5.0.6 on 2024-06-08 21:58

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_item_table_alter_recipe_table_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="fridge",
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
                ("fr_name", models.CharField(max_length=100, verbose_name="it_name")),
            ],
        ),
        migrations.CreateModel(
            name="items",
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
                ("it_name", models.CharField(max_length=100, verbose_name="it_name")),
            ],
            options={
                "db_table": "items",
            },
        ),
        migrations.CreateModel(
            name="publish",
            fields=[
                (
                    "pub_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="pub_id"
                    ),
                ),
                ("pub_date", models.DateField(verbose_name="pub_date")),
            ],
        ),
        migrations.CreateModel(
            name="recipes",
            fields=[
                (
                    "re_id",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="re_id"
                    ),
                ),
                ("re_name", models.CharField(max_length=120, verbose_name="re_name")),
                (
                    "re_step",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1000),
                        blank=True,
                        size=None,
                    ),
                ),
                ("re_minute", models.IntegerField(verbose_name="re_id")),
            ],
            options={
                "db_table": "recipes",
            },
        ),
        migrations.DeleteModel(
            name="Item",
        ),
        migrations.DeleteModel(
            name="Recipe",
        ),
        migrations.RemoveField(
            model_name="users",
            name="id",
        ),
        migrations.RemoveField(
            model_name="users",
            name="user_email",
        ),
        migrations.AddField(
            model_name="users",
            name="user_mail",
            field=models.EmailField(
                default="invalid",
                max_length=60,
                primary_key=True,
                serialize=False,
                verbose_name="user_mail",
            ),
        ),
        migrations.AddField(
            model_name="publish",
            name="pub_publisher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.users"
            ),
        ),
    ]
