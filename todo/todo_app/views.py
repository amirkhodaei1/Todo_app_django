from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo

# Create your views here.
class TodoListView(ListView):
    ordering='-created_date'
    context_object_name = 'todos'
    queryset = Todo.objects.filter(status=True)
