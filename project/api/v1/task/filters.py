from apps.task.models import Task, TaskTypeChoices
from django_filters import ChoiceFilter, FilterSet


class TaskFilter(FilterSet):
    """
    Возвращает задачи согласно фильтрации

    по статусам
    /api/v1/task/?status=OPEN
    """

    status = ChoiceFilter(choices=TaskTypeChoices.choices)
