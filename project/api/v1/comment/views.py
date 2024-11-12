from api.v1.comment.filters import CommentFilter
from api.v1.comment.serializers import CommentReadSerializer, CommentWriteSerializer
from api.v1.user.views import AuthViewSet
from apps.comment.models import Comment
from apps.helpers.permissions import (
    IsAdministratorOrSuperUser,
    IsPerformerTaskUser,
    IsSuperUser,
)
from apps.helpers.viewsets import CRUDExtendedModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter


class CommentViewSet(CRUDExtendedModelViewSet):
    """
    retrieve:
    Возвращает комментарий.

    list:
    Возвращает список всех комментариев.

    create:
    Создает новый комментарий.

    update:
    Обновляет комментарий.

    partial_update:
    Обновляет часть данных комментария.

    destroy:
    Удаляет комменатрий.
    """

    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    serializer_class_map = {
        "list": CommentReadSerializer,
        "create": CommentWriteSerializer,
        "update": CommentWriteSerializer,
        "partial_update": CommentWriteSerializer,
        "retrieve": CommentReadSerializer,
    }
    filterset_class = CommentFilter
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
