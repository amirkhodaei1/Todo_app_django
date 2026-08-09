from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView,UpdateView,DeleteView
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


# Create your views here.
class TodoListView(LoginRequiredMixin,ListView):
    ordering = "-created_date"
    context_object_name = "todos"
    queryset = Todo.objects.all()


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    success_url = "/"
    # fields = ["user", "title", "content", "status", "category", "published_date"]
    template_name = "todo_app/form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoEditView(LoginRequiredMixin, UpdateView):

    model = Todo

    form_class = TodoForm

    success_url = "/"

    # fields = ["user", "title", "content", "status", "category", "published_date"]

    template_name = "todo_app/form.html"

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)


class TodoDeleteView(LoginRequiredMixin, DeleteView):

    model = Todo
    success_url = "/"

    # fields = ["user", "title", "content", "status", "category", "published_date"]

    # template_name='form.html'
