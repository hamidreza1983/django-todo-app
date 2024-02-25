from ..forms import CustomUserCreation
from django.views.generic import CreateView


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreation
    success_url = "/accounts/login/"
