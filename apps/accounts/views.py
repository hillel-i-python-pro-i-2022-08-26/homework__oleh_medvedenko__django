from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views import generic

from apps.accounts.forms import UserCreationFormCustom


class SignUpView(generic.CreateView):
    form_class = UserCreationFormCustom
    template_name = "registration/signup.html"
    success_url = reverse_lazy("accounts:login")


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("base_app:main_page")


class LogoutUserView(LogoutView):
    next_page = reverse_lazy("base_app:main_page")
