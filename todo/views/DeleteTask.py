from django.views.generic import DeleteView
from todo.models import Task


class DeleteTask(DeleteView):
    model = Task
    success_url = "/"
