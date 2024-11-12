from typing import Final

from apps.file.models import File
from apps.helpers.models import CreatedModel, UUIDModel, enum_max_length
from apps.user.admin import User
from django.db import models

_FIELD_MAX_LENGTH: Final = 150


class TaskTypeChoices(models.TextChoices):
    COMPLETED = "COMPLETED", "Выполнена"
    OPEN = "OPEN", "Открыта"


class Task(UUIDModel, CreatedModel):
    name = models.CharField("Название", max_length=_FIELD_MAX_LENGTH, default="")
    description = models.TextField("Описание задачи", default="", null=True, blank=True)
    status = models.CharField(
        "Статус задачи",
        max_length=enum_max_length(TaskTypeChoices),
        choices=TaskTypeChoices.choices,
        default=TaskTypeChoices.OPEN,
    )
    due_date = models.DateTimeField("Дедлайн задачи")
    attachments = models.ManyToManyField(
        File,
        verbose_name="Файлы",
        related_name="attachments",
        blank=True,
    )
    assignees = models.ManyToManyField(
        User,
        verbose_name="Назначенные исполнители на задачу",
        related_name="tasks",
        blank=True,
    )
    creator = models.ForeignKey(
        User,
        verbose_name="Инициатор(создатель) задачи",
        related_name="created_tasks",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return f"{self.name}"
