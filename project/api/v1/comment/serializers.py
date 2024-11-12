from apps.comment.models import Comment
from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers


class CommentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "task",
            "created_at",
        )


class CommentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "task",
        )
