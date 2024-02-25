from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
)
from .serializer import TaskSerializer 
from ...models import Task


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]