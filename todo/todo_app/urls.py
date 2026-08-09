from django.urls import path
from . import views
app_name='todo_app'
urlpatterns = [
    path("", views.TodoListView.as_view(),name="todo-list"),
    path('create/',views.TodoCreateView.as_view(),name="todo-create"),
    path('<int:pk>/edit',views.TodoEditView.as_view(),name="todo-edit"),
    path('<int:pk>/delete',views.TodoDeleteView.as_view(),name="todo-delete")
]