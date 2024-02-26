from rest_framework import serializers
from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        max_length=50, source="user.email", read_only=True
    )

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "image", "email"]
