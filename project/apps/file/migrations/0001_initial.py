# Generated by Django 5.1.3 on 2024-11-11 18:12

import uuid

import apps.file.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        null=True,
                        verbose_name="deleted at",
                    ),
                ),
                ("file", models.FileField(upload_to=apps.file.models.directory_path)),
            ],
            options={
                "verbose_name": "Файл",
                "verbose_name_plural": "Файлы",
            },
        ),
    ]