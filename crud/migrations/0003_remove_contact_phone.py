# Generated by Django 4.2.3 on 2023-08-02 03:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0002_rename_description_blog_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="phone",
        ),
    ]