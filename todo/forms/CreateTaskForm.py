from django import forms
from todo.models import Task


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title",)
