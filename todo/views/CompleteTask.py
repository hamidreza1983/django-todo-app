from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Task


class CompleteTask(LoginRequiredMixin, View):
    model = Task
    success_url = "/"

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)
