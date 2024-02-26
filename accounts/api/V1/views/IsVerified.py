from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from accounts.models import CustomeUser
from django.shortcuts import get_object_or_404

from rest_framework_simplejwt.tokens import AccessToken


class IsVerified(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomeUser, id=user_id)
            user.is_verified = True
            user.save()
            return Response({"detail": "your account veridied successfully"})
        except:
            return Response(
                {
                    "detail": "your token was expired or changed structure",
                    "resend_email": "http://127.0.0.1:8000/accounts/api/V1/resend",
                }
            )
