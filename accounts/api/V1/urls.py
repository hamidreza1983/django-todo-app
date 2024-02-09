from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'api-V1-accounts'

urlpatterns =[
    path('registration/', RegistrationView.as_view(), name = 'registration'),
    path('token/login/', CustomeObtainAuthToken.as_view(), name = 'login'),
    path('token/logout/', DestroyAuthToken.as_view(), name = 'logout'),
    path('change-password/', ChangePasswordView.as_view(), name = 'change-password'),

    #jwt token:)
    path('token/create/', Customejwtview.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]