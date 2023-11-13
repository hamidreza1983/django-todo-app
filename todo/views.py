from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(TemplateView):
    template_name = 'todo/index.html'
    
