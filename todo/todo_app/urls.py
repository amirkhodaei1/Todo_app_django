from django.urls import include, path

from . import views

app_name = "todo_app"
urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo-list"),
    path("create/", views.TodoCreateView.as_view(), name="todo-create"),
    path("<int:pk>/edit", views.TodoEditView.as_view(), name="todo-edit"),
    path("<int:pk>/delete", views.TodoDeleteView.as_view(), name="todo-delete"),
    path("api/v1/", include("todo_app.api.v1.urls", "api-v1"), name="api-v1"),
]
