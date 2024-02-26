from django.urls import path,include
from .views import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

app_name = 'api-v1'

urlpatterns = [
    path('tasks/',TaskView.as_view({'get': 'list','post':'create'}),name='tasks'),
    path('tasks/<int:pk>',TaskView.as_view({'get': 'retrieve','put':'update', 'delete':'destroy'}),name='task-detail'),
]