from django.shortcuts import render
from django.views.generic import FormView



class HomeView(FormView):
    template_name = 'todo/index.html'
    
