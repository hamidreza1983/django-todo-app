from rest_framework import viewsets
from .serializer import *
from ...models import *
from rest_framework.permissions import IsAuthenticated




class TaskView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()