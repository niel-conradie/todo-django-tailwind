from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    A form for user registration based on the CustomUser model.

    Inherits all fields and methods from the UserCreationForm class and adds additional customization
    specific to the CustomUser model.

    Parameters:
    - UserCreationForm (class): The base user creation form that provides the basic user fields and methods.
    """

    class Meta:
        """
        A class used to define metadata for the CustomUserCreationForm form.

        Fields:
        - model (class): The model that the form will be based on, which is the CustomUser model.
        - fields (tuple): The fields that will be included in the form, which are the email and username fields.
        """

        model = CustomUser
        fields = (
            "email",
            "username",
        )
