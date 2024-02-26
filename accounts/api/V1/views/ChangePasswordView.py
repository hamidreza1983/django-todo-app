from rest_framework.generics import GenericAPIView
from accounts.api.V1.serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ChangePasswordView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.check_old_password(request, serializer.validated_data)
        serializer.set_new_password(request, serializer.validated_data)
        token = serializer.create_new_token(
            request, serializer.validated_data
        )

        return Response(
            data={
                "detail": "change password successfuly",
                "token": token.key,
            },
            status=status.HTTP_200_OK,
        )
