from api.v1.comment.filters import CommentFilter
from api.v1.comment.serializers import CommentReadSerializer, CommentWriteSerializer
from apps.comment.models import Comment
from apps.helpers.viewsets import CRDExtendedModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import OrderingFilter, SearchFilter


class CommentViewSet(CRDExtendedModelViewSet):
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
