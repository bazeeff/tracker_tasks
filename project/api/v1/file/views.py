from apps.file.models import File
from apps.helpers.batchmixin import DeleteBatchMixin
from apps.helpers.viewsets import ExtendedModelViewSet
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser

from .serializers import FileSerializer


class FileViewSet(ExtendedModelViewSet, DeleteBatchMixin):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)
