# Generated by Django 4.2.3 on 2023-07-26 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="blog",
            old_name="description",
            new_name="content",
        ),
        migrations.RenameField(
            model_name="blog",
            old_name="name",
            new_name="user_name",
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=300),
        ),
    ]
