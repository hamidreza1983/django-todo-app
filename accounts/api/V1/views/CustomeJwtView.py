from accounts.api.V1.serializer import CustomeObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class CustomeJwtView(TokenObtainPairView):

    serializer_class = CustomeObtainPairSerializer
