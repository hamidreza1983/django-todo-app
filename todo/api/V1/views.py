from rest_framework import viewsets
from .serializer import *
from ...models import *





class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()