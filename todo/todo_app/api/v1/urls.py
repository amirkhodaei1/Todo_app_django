from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todo_app.api.v1.views import TodoModelViewSet

app_name = "api-v1"

router = DefaultRouter()
router.include_format_suffixes = False
router.register("posts", TodoModelViewSet, basename="todo")
urlpatterns = [
    path("", include(router.urls)),
]
