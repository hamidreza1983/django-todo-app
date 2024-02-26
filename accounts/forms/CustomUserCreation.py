from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomeUser


class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ["email", "username", "password1", "password2"]
