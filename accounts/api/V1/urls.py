from django.urls import path, include
from .views import *

app_name = 'api-V1-accounts'

urlpatterns =[
    path('registration/', RegistrationView.as_view(), name = 'registration'),
]