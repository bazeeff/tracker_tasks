from api.v1.comment.serializers import CommentReadSerializer
from api.v1.file.serializers import FileSerializer
from api.v1.user.serializers import UserReadSerializer
from apps.comment.models import Comment
from apps.task.models import Task
from rest_framework import serializers


class TaskReadSerializer(serializers.ModelSerializer):
    attachments = FileSerializer(many=True)
    assignees = UserReadSerializer(many=True)
    comments = serializers.SerializerMethodField()
    creator = UserReadSerializer(read_only=True)

    select_related_fields = ("creator",)
    prefetch_related_fields = (
        "attachments",
        "assignees",
    )

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "status",
            "due_date",
            "attachments",
            "assignees",
            "creator",
            "comments",
            "created_at",
        )

    def get_comments(self, instance):
        comments = Comment.objects.filter(task=instance)
        return CommentReadSerializer(comments, many=True).data


class TaskCompactReadSerializer(serializers.ModelSerializer):
    creator = UserReadSerializer(read_only=True)

    select_related_fields = ("creator",)

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "status",
            "due_date",
            "creator",
            "created_at",
        )


class TaskWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "status",
            "due_date",
            "attachments",
            "assignees",
        )
