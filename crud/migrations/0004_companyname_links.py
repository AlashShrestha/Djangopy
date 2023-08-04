# Generated by Django 4.2.3 on 2023-08-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0003_remove_contact_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="CompanyName",
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
                ("name", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Links",
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
                ("url", models.URLField()),
                ("icon", models.CharField(max_length=100)),
            ],
        ),
    ]
