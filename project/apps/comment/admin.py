from apps.comment.models import Comment
from django.contrib import admin


@admin.register(Comment)
class FileAdmin(admin.ModelAdmin):
    pass  # noqa: WPS420 WPS604
