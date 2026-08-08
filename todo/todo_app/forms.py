from django import forms
from .models import Todo


class PostForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ["title", "content", "status", "category", "published_date"]
