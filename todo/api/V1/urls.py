from rest_framework.routers import DefaultRouter
from todo.api.V1.views import TaskView

app_name = "api-v1"

router = DefaultRouter()
router.register("tasks", TaskView, basename="Tasks")

urlpatterns = router.urls
