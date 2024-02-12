from django.views.generic import UpdateView
from ..models import Task

class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/update_task.html'
    fields = ['title']
    success_url = '/'
    context_object_name = 'task'