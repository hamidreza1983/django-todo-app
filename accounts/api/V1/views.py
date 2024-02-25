from rest_framework.generics import GenericAPIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



class RegistrationView(GenericAPIView):

    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'email':serializer.validated_data['email']

            }
        return Response(data, status=status.HTTP_201_CREATED)
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
    
class DestroyAuthToken(APIView):

    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Customejwtview(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


class ChangePasswordView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.check_old_password(request, serializer.validated_data)
        serializer.set_new_password(request, serializer.validated_data)
        token = serializer.create_new_token(request, serializer.validated_data)

        return Response(
            data={"detail": "password change successfully.", "token": token.key},
            status=status.HTTP_200_OK,
        )



class IsVerifiedView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomeUser, id=user_id)
            user.is_verified = True
            user.save()
            return Response({"detail": "your account verified successfully"})
        except:
            return Response(
                {
                    "detail": "your token may be expired or changed structure :)))",
                    "resend email": "http://127.0.0.1:8080/accounts/api/V1/resend",
                }
            )


class ResendEmailView(GenericAPIView):
    serializer_class = ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_verified:
            return Response({"detail": "your email is already verified"})
        token = self.get_tokens_for_user(user)
        message = EmailMessage(
            "email/email.html",
            {"token": token},
            "hesam@ghadami.com",
            to=[serializer.validated_data["email"]],
        )
        email = SendEmailWithThreading(message)
        email.start()
        return Response({"detail": "email Resend for you..."})

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    

class ResetPasswordView(GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        # email  = request.data.get('email')
            # user = CustomeUser.objects.get(email=email)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token = self.get_tokens_for_user(user)
            message = EmailMessage(
            "email/reset.html",
            {"token": token},
            "hesam@ghadami.com",
            to=[serializer.validated_data["email"]],)
            
            Email = SendEmailWithThreading(message)
            Email.start()
            return Response({"detail": "reset password email has sent for you..."})



    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ConfirmResetPasswordView(GenericAPIView):

    serializer_class = ConfirmResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_data = AccessToken(kwargs.get("token"))
            user_id = user_data["user_id"]
            user = get_object_or_404(CustomeUser, id=user_id)

            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.set_new_password(user, serializer.validated_data)
            token = serializer.create_new_token(user, serializer.validated_data)

            return Response(
            data={"detail": "password change successfully.", "token": token.key},
            status=status.HTTP_200_OK,
        )
        except:
            return Response(
                {
                    "detail": "your token may be expired or changed structure :)))",
                    # "resend email": "http://127.0.0.1:8080/accounts/api/V1/resend",
                }
            )