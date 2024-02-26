from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

from rest_framework.authtoken.models import Token


class PasswordChangeSerializer(serializers.Serializer):

    old_password = serializers.CharField(max_length=20)
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

    def check_old_password(self, request, attrs: dict):

        old_pass = attrs.get("old_password")
        pass1 = attrs.get("new_password1")
        user = request.user
        if not user.check_password(old_pass):
            raise serializers.ValidationError(
                {"detail": "old_password is not confirmed"}
            )

        if old_pass == pass1:
            raise serializers.ValidationError(
                {"detail": "old_password can not same as new pass"}
            )

        return attrs

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
        except:
            Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        return token
