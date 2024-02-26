from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from accounts.api.V1.views import (
    RegistrationView,
    CustomeObtainAuthToken,
    DestroyAuthToken,
    ChangePasswordView,
    IsVerifiedView,
    ResetPasswordView,
    ResendEmailView,
    ResetPasswordEmailView
    )

app_name = "api-V1-accounts"

urlpatterns = [
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("token/login/", CustomeObtainAuthToken.as_view(), name="login"),
    path("token/logout/", DestroyAuthToken.as_view(), name="logout"),
    path("change-password/",ChangePasswordView.as_view(),name="change-password"),
     path("is-verified/<str:token>", IsVerifiedView.as_view(), name="is-verification"),
    path("resend/", ResendEmailView.as_view(), name="resend"),
    path("reset-password-email/",ResetPasswordEmailView.as_view(),
        name="reset-password-email",),
    path("reset-password/<str:token>", ResetPasswordView.as_view(), 
        name="reset-password"),
    # jwt token:)
    path(
        "token/create/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
