from apps.helpers.serializers import EnumSerializer
from apps.helpers.viewsets import CRDExtendedModelViewSet
from apps.task.models import Task, TaskTypeChoices
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from .filters import TaskFilter
from .serializers import TaskReadSerializer, TaskWriteSerializer


class TaskViewSet(CRDExtendedModelViewSet):
    """
    retrieve:
    Возвращает информацию о задаче.

    list:
    Возвращает список всех задач.
    /api/v1/task/?status=    возвращает список проектов по статусу
    /api/v1/task/?search=    поиск по названию проекта, имени участника проекта

    create:
    Создает новую задачу.

    update:
    Обновляет данные задачи.

    partial_update:
    Обновляет часть данных задачи.

    destroy:
    Удаляет задачу.
    """

    queryset = Task.objects.all()
    serializer_class = TaskReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = TaskFilter
    serializer_class_map = {
        "list": TaskReadSerializer,
        "create": TaskWriteSerializer,
        "update": TaskWriteSerializer,
        "partial_update": TaskWriteSerializer,
        "retrieve": TaskReadSerializer,
    }

    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(responses={200: EnumSerializer})
    @action(methods=["get"], detail=False)
    def status(self, request):
        """Возвращает возможные типы статусов задачи"""
        return Response(EnumSerializer(TaskTypeChoices, many=True).data)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
