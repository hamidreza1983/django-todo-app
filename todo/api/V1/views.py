from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.api.V1.serializer import TaskSerializer
from todo.models import Task


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
