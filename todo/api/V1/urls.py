from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('tasks', TaskView, basename='Tasks')

urlpatterns = router.urls


