from rest_framework.response import Response
from .serializer import TaskSerializer
from ...models import Task
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .permissions import *

class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [JustAuthenticatedUser]
    ordering_fields = ['created_date']
    

