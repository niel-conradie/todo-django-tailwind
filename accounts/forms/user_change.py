from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


CustomUser = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating user information, specifically for the CustomUser model.

    Inherits all fields and methods from the UserChangeForm class and adds additional customization
    specific to the CustomUser model.

    Parameters:
    - UserChangeForm (class): The base user change form that provides the basic user fields and methods.

    Class:
    - Meta: Provides metadata for the CustomUserChangeForm class in Django.
    """

    class Meta:
        """
        A class used to define metadata for the CustomUserChangeForm form.

        Fields:
        - model (class): The model that the form will be based on, which is the CustomUser model.
        - fields (tuple): The fields that will be included in the form, which are the email and username fields.
        """

        model = CustomUser
        fields = (
            "email",
            "username",
        )
