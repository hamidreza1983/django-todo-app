from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.shortcut import get_object_or_404
from rest_framework.authtoken.models import Token
from accounts.models import CustomeUser



class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs


class ResetPasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(max_length=20)
    new_password2 = serializers.CharField(max_length=20)

    def validate(self, attrs):
        pass1 = attrs.get("new_password1")
        pass2 = attrs.get("new_password2")

        if pass1 != pass2:
            raise serializers.ValidationError(
                {"detail": "pass1 and pass2 must be the same"}
            )

        return super().validate(attrs)

    def set_new_password(self, request, attrs: dict):
        pass1 = attrs.get("new_password1")
        user = request.user
        try:

            validate_password(pass1)

        except exceptions.ValidationError as e:

            raise serializers.ValidationError({"detail": list(e.messages)})

        user.set_password(pass1)
        user.save()
        return attrs

    def create_new_token(self, request, attrs: dict):
        user = request.user

        try:
            user.auth_token.delete()
            Token.objects.create(user=user)
        except Exception:
            Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        return token