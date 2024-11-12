from apps.task.models import Task
from django.contrib import admin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
