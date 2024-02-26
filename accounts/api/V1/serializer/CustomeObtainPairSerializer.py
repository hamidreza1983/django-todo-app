from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class CustomeObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs) :
        validated_data = super().validate(attrs)
         
        if not self.user.is_verified:
            msg = ('your account is not verified.')
            raise serializers.ValidationError(msg, code='authorization')
                     
        validated_data['id'] = self.user.id
        validated_data['email'] = self.user.email
        return validated_data
    