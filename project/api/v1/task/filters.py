from apps.task.models import Task, TaskTypeChoices
from django_filters import ChoiceFilter, FilterSet, CharFilter


class TaskFilter(FilterSet):
    """
    Возвращает задачи согласно фильтрации

    по статусам
    /api/v1/task/?status=OPEN
    """

    status = ChoiceFilter(choices=TaskTypeChoices.choices)
    name = CharFilter(field_name="name", lookup_expr="icontains")
