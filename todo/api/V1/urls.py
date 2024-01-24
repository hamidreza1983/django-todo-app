from django.urls import path, include
from .views import TodoView

app_name = 'api-v1-todo'

urlpatterns = [
    path('todo', TodoView.as_view(), name='todo')
]