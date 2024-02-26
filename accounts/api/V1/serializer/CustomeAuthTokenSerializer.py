from rest_framework import serializers
from django.contrib.auth import authenticate




class CustomeAuthTokenSerializer(serializers.Serializer):
        email = serializers.EmailField(
        label=("Email"),
        write_only=True
    )
        password = serializers.CharField(
            label=("Password"),
            style={'input_type': 'password'},
            trim_whitespace=False,
            write_only=True
        )
        token = serializers.CharField(
            label=("Token"),
            read_only=True
        )

        def validate(self, attrs):
            email = attrs.get('email')
            password = attrs.get('password')

            if email and password:
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)

                # The authenticate call simply returns None for is_active=False
                # users. (Assuming the default ModelBackend authentication
                # backend.)
                if not user:
                    msg = ('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg, code='authorization')
                
                if not user.is_verified:
                    msg = ('your account is not verified.')
                    raise serializers.ValidationError(msg, code='authorization')
                     
            else:
                msg = ('Must include "email" and "password".')
                raise serializers.ValidationError(msg, code='authorization')
            attrs['user'] = user
            return attrs
