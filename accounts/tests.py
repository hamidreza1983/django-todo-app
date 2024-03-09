from django.test import TestCase
from django.urls import resolve, reverse
from accounts.views import(
    LoginView,
    LogOutView,
    SignUpView,
)

class TestAccountURL(TestCase):
    '''Tests for the accounts/urls.py file'''
    def test_LoginUrl(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, LoginView)
    
    def test_LogOutUrl(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, LogOutView)

    def test_SignUpUrl(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)