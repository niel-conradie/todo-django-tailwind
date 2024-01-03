from django.contrib.auth.models import AbstractUser

from utils.models import UUIDModel


class CustomUser(AbstractUser, UUIDModel):
    """
    Represents a custom user model with a UUID as the primary key.

    Inherits from the `AbstractUser` model, which provides the basic user fields and methods,
    and includes the `UUIDModel` model, which adds a UUID field to the model.

    Parameters:
    - AbstractUser (class): An abstract base class implementing a fully featured User model with admin-compliant permissions.
    - UUIDModel (class): The model that adds a UUID field to the model.

    Methods:
    - __str__(self): Returns a string representation of the object.
    """

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
        - str (string): The string representation of the object.
        """
        return self.username
