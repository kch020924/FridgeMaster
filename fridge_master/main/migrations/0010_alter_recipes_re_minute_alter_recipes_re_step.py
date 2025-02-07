# Generated by Django 5.0.6 on 2024-06-08 23:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_publish_pub_re_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipes",
            name="re_minute",
            field=models.IntegerField(verbose_name="re_minute"),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="re_step",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1000),
                blank=True,
                size=None,
                verbose_name="re_step",
            ),
        ),
    ]
