from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


CustomUser = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
        )
