# Generated by Django 5.1.3 on 2024-11-11 23:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="user",
            new_name="author",
        ),
    ]