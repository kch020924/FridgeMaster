# Generated by Django 5.0.6 on 2024-06-08 12:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_rename_new_item_alter_item_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="item",
            table="item",
        ),
        migrations.AlterModelTable(
            name="recipe",
            table="recipe",
        ),
        migrations.AlterModelTable(
            name="users",
            table="users",
        ),
    ]
