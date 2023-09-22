from django.contrib.auth.views import LoginView

from accounts.forms import CustomAuthenticationForm


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "accounts/login.html"