from accounts.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.detail[:5]

    def get_absolute_api_url(self):
        return reverse("todo_app:api-v1:todo-detail", kwargs={"pk": self.pk})

    class Meta:
        order_with_respect_to = "user"
