from django.contrib.auth import get_user_model
from django.db import models

from todo.models import DayModel

from utils.models import UUIDModel


CustomUser = get_user_model()


class TaskModel(UUIDModel):
    """
    Represents a model for tasks in a Django application.

    Parameters:
    - UUIDModel (class): The model that adds a UUID field to the model.

    Fields:
    - title (CharField): The title of the task.
    - day (ForeignKey): The day associated with the task.
    - time_start (TimeField): The start time of the task.
    - time_end (TimeField): The end time of the task.
    - created_by (ForeignKey): The user who created the task.
    - created_at (DateTimeField): The date and time when the task was created.
    - modified_at (DateTimeField): The date and time when the task was last modified.
    - status (BooleanField): The status of the task (active or inactive).

    Class:
    - Meta: Provides metadata for the TaskModel class in Django.

    Methods:
    - __str__(self): Returns a string representation of the object.
    """

    title = models.CharField(
        max_length=15,
    )

    day = models.ForeignKey(
        DayModel,
        related_name="tasks",
        on_delete=models.CASCADE,
    )

    time_start = models.TimeField()

    time_end = models.TimeField()

    created_by = models.ForeignKey(
        CustomUser,
        related_name="tasks",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )

    STATUS_CHOICES = (
        (True, "Active"),
        (False, "Inactive"),
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=True,
    )

    class Meta:
        """
        Provides metadata for the TaskModel class in Django.

        Options:
        - ordering (tuple): Specifies the default ordering of the tasks based on the created_at field in descending order.
        - verbose_name (str): Specifies the singular name for the model, which will be displayed in the Django admin interface.
        - verbose_name_plural (str): Specifies the plural name for the model, which will be displayed in the Django admin interface.
        """

        ordering = ("-created_at",)
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
        - str (string): The string representation of the object.
        """

        return self.title
