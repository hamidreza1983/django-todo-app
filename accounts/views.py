from django.shortcuts import redirect
from .forms import CustomUserCreation
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticationForm
from django.views.generic import FormView, CreateView, TemplateView, UpdateView
from .models import  Profile

class LoginView(FormView):
     template_name = 'registration/login.html'
     form_class = AuthenticationForm
     success_url = '/'
     def form_valid(self, form):
         email = self.request.POST.get('email')
         password = self.request.POST.get('password')
         user = authenticate(email=email, password=password)
         if user is not None:
              login(self.request, user)
              return super().form_valid(form)
         


class LogOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')



class SignUpView(CreateView):
     template_name = 'registration/signup.html'
     form_class = CustomUserCreation
     success_url = '/accounts/login/'
     
     def form_valid(self, form):
        form.save()
        email = self.request.POST.get('email')
        password = self.request.POST.get('password1')   
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request,user)
            return redirect('/')
        
     def form_invalid(self, form):
        return super().form_invalid(form)
     



class EditProfileView(UpdateView):
    template_name = 'registration/edit_profile.html'
    model = Profile
    fields = [ 'user','emil' ]
    success_url = '/'