from django.urls import path
from todo.api.V1.views import TaskView


app_name = "api-v1"

urlpatterns = [
    path(
        "tasks/",
        TaskView.as_view({"get": "list", "post": "create"}),
        name="tasks",
    ),
    path(
        "tasks/<int:pk>",
        TaskView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="task-detail",
    ),
]
