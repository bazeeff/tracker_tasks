from apps.helpers.models import CreatedModel, UUIDModel
from apps.task.models import Task
from apps.user.admin import User
from django.db import models


class Comment(UUIDModel, CreatedModel):
    text = models.TextField("Текст комментария", null=True, blank=True, default="")
    author = models.ForeignKey(
        User,
        verbose_name="Владелец комментария(Пользователь)",
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.CASCADE)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Комментарий к задаче"
        verbose_name_plural = "Комментарии к задачам"

    def __str__(self):
        return f"{self.task.name} {self.text}"
