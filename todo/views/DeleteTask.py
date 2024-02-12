from django.views.generic import DeleteView
from ..models import Task

class DeleteTask(DeleteView):
    model = Task
    success_url = '/'
