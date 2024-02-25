from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView


class LogOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')