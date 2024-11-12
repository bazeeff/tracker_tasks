from api.v1.user.serializers import UserReadSerializer
from apps.comment.models import Comment
from rest_framework import serializers


class CommentReadSerializer(serializers.ModelSerializer):
    author = UserReadSerializer()

    select_related_fields = ("author",)

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
            "task",
        )
