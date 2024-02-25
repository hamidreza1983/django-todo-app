from django.urls import path, include
from todo.api.V1.views import TodoView
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("tasks", TodoView, basename="Tasks")

urlpatterns = router.urls
