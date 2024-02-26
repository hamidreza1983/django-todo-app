from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


app_name = 'api-v1-accounts'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name = 'registration'),
    path('token/login/', ObtainAuthToken.as_view(), name = 'login'),
    path('token/logout/', DestroyAuthToken.as_view(), name = 'logout'),
    path('change_password/',ChangePasswordView.as_view(), name = 'change_password'),
    path('profile/',ProfileView.as_view(), name = 'profile'),
    # path('verification',VerificationView.as_view(), name = 'verification'),
    path('is-verified/<str:token>',IsVerified.as_view(), name = 'is_verified'),
    path('resend/',ResendEmailView.as_view(), name = 'resend'),
    path('reset-password',ResetPasswordView.as_view(), name ='reset_password'),
    path('reset-password-email/',ResetPasswordEmailView.as_view(), name = 'reset_password_email'),

    path('token/create/', CustomeJwtView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
