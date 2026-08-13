from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("todo", views.TodoModelViewSet, basename="todo")
urlpatterns = router.urls

app_name = "todo-api-v1"

