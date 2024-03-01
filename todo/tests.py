from django.test import TestCase
from django.urls import resolve, reverse
from todo.views import(
    HomeView,
    DeleteTask,
    CompleteTask,
    UpdateTask,
)

class TestTodoURL(TestCase):
    '''Tests for the todo/urls.py file'''
    def test_HomeUrl(self):
        url = reverse('todo:home')
        self.assertEqual(resolve(url).func.view_class, HomeView)
    
    def test_DeleteTaskUrl(self):
        url = reverse('todo:delete_task', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, DeleteTask)

    def test_CompleteTaskUrl(self):
        url = reverse('todo:complete_task', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, CompleteTask)

    def test_UpdateTaskUrl(self):
        url = reverse('todo:update_task', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, UpdateTask)

    