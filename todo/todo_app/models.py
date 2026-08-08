from django.db import models
from accounts.models import User

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

    class Meta:
        order_with_respect_to = "user"
