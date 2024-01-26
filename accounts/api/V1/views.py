from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken

class RegistrationView(GenericAPIView):
    
    serializer_class = RegisterationSerializer
    
    def post(self, request, *args, **kwargs):

        serializer = RegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print (serializer.validated_data)
            data = {
                'email': serializer.validated_data['email']
            }
            return Response(data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomeObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomeAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })