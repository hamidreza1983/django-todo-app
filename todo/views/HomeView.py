from django.shortcuts import get_object_or_404, redirect
from accounts.models import CustomeUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from todo.models import Task
from todo.forms import CreateTaskForm



class HomeView(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        User = get_object_or_404(CustomeUser, email=self.request.user.email)
        task = Task.objects.filter(user=User)
        return task
    
    def post(self, request, *args, **kwargs):
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect ('/')
