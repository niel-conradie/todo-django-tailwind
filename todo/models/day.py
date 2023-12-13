from django.db import models

from utils.models import UUIDModel


class DayModel(UUIDModel):
    """
    Represents a model for days in a Django application.

    Parameters:
    - UUIDModel (class): The model that adds a UUID field to the model.

    Fields:
    - title (CharField): A field that stores the day of the week as a string.
    - slug (SlugField): A field that stores a URL-friendly representation of the title.

    Class:
    - Meta: Provides metadata for the TaskModel class in Django.

    Methods:
    - __str__(): Returns a string representation of the object.
    """

    TITLE_CHOICES = (
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    )
    title = models.CharField(
        max_length=9,
        choices=TITLE_CHOICES,
        unique=True,
    )

    slug = models.SlugField()

    class Meta:
        """
        Provides metadata for the TaskModel class in Django.

        Fields:
        - verbose_name (str): Specifies the singular name for the model, which will be displayed in the Django admin interface.
        - verbose_name_plural (str): Specifies the plural name for the model, which will be displayed in the Django admin interface.
        """

        verbose_name = "Day"
        verbose_name_plural = "Days"

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
        - str (string): The string representation of the object.
        """

        return self.title
