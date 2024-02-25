from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from accounts.models import CustomeUser


class RegisterationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = CustomeUser
        fields = ["email", "username", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password1") != attrs.get("password"):
            raise serializers.ValidationError(
                {"detail": "password dose not confirmed"}
            )
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"detail": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return CustomeUser.objects.create_user(**validated_data)
