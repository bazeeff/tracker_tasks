from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .celery.views import CeleryResultView
from .comment.views import CommentViewSet
from .file.views import FileViewSet
from .settings.views import SettingsViewSet
from .task.views import TaskViewSet
from .user.views import UserViewSet

router = routers.DefaultRouter()
router.register("settings", SettingsViewSet, basename="settings")
router.register("file", FileViewSet, basename="file")
router.register("user", UserViewSet, basename="user")
router.register("task", TaskViewSet, basename="task")
router.register("comment", CommentViewSet, basename="comment")

schema_view = get_schema_view(
    openapi.Info(
        title="Always data API",
        default_version="v1",
        description="Routes of Always data project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger(<str:format>.json|.yaml)/",
        schema_view.without_ui(),
        name="schema-json",
    ),
    path("swagger/", schema_view.with_ui("swagger"), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc"), name="schema-redoc"),
    path("", include((router.urls, "api-root")), name="api-root"),
    path("celery/result/<pk>/", CeleryResultView.as_view()),
]
