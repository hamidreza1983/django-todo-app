from .views import *
from rest_framework.routers import DefaultRouter


app_name = 'api-v1'

router = DefaultRouter()
router.register('todo', TaskView, basename='todo')
urlpatterns = router.urls