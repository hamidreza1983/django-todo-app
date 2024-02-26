from rest_framework.generics import GenericAPIView
from accounts.api.V1.serializer import ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken


class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.set_new_password(request, serializer.validated_data)
            token = serializer.create_new_token(
                request, serializer.validated_data
            )

            return Response(
                data={
                    "detail": "password change successfully.",
                    "token": token.key,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return Response(
                {
                    "detail": "your token may be expired or changed structure...",
                    "resend email": "http://127.0.0.1:8000/accounts/api/V1/resend",
                }
            )
