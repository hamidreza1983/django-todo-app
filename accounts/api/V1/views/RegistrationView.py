from rest_framework.generics import GenericAPIView
from accounts.api.V1.serializer import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from accounts.api.V1.multi_threading import SendEmailWithThreading
from mail_templated import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomeUser


class RegistrationView(GenericAPIView):
    """
    this class is for create user
    """

    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                CustomeUser, email=serializer.validated_data["email"]
            )
            token = self.get_tokens_for_user(user)
            message = EmailMessage(
                "email/email.html",
                {"token": token},
                "fatemeh@admin.com.com",
                to=[serializer.validated_data["email"]],
            )
            email = SendEmailWithThreading(message)
            email.start()
            return Response({"detail": "email sent for your verification...!"})

            # print (serializer.validated_data)
            # data = {
            #     'email': serializer.validated_data['email']
            # }
            # return Response(data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    