from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from ..serializer import CustomeAuthTokenSerializer
from rest_framework.response import Response


class CustomeObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomeAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"token": token.key, "user_id": user.pk, "email": user.email}
        )
