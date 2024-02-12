from django.shortcuts import get_object_or_404
from accounts.models import CustomeUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    def get_queryset(self):
        User = get_object_or_404(CustomeUser, email=self.request.user.email)
        return User.user_tasks()
