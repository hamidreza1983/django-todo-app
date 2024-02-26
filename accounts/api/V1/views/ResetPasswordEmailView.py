from rest_framework.generics import GenericAPIView
from accounts.api.V1.serializer import *
from rest_framework.response import Response
from accounts.api.V1.multi_threading import SendEmailWithThreading
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken





class ResetPasswordEmailView(GenericAPIView):

    
    serializer_class = ResetPasswordEmailSerializer


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = self.get_tokens_for_user(user)
        message = EmailMessage(
            "email/resetemail.html",
            {"token": token},
            "negin@gmail.com",
            to=[serializer.validated_data["email"]],
        )
        email = SendEmailWithThreading(message)
        email.start()
        return Response({"detail": "email Resend for you..."})
    
    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)