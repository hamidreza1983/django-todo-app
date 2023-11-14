from django.shortcuts import get_object_or_404
from accounts.models import CustomeUser
from django.views.generic import ListView, UpdateView, DeleteView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import UpdateTask



class HomeView(LoginRequiredMixin, ListView):
    form = Task
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        User = get_object_or_404(CustomeUser, email=self.request.user.email)
        return User.user_tasks()



class DeleteTask(DeleteView):
    model = Task
    success_url = '/'



class CompleteTask(UpdateView):
    pass



class UpdateTask(UpdateView):
    model = Task
    template_name = 'todo/update_task.html'
    form_class = UpdateTask
    success_url = '/'
    context_object_name = 'task'
