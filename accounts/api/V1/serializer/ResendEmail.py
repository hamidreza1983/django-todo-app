from djnago.shortcut import get_object_or_404
from rest_framework import serializers
from accounts.models import CustomeUser


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs
    