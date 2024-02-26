from django.shortcuts import get_object_or_404, redirect
from accounts.models import CustomeUser
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    View,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import CreateTaskForm


class HomeView(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        User = get_object_or_404(CustomeUser, email=self.request.user.email)
        return User.user_tasks()
    
    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect ('/')




class DeleteTask(DeleteView):
    model = Task
    success_url = '/'





class CompleteTask(LoginRequiredMixin, View):
    model = Task
    success_url = '/'

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)



class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/update_task.html'
    fields = ['title']
    success_url = '/'
    context_object_name = 'task'
