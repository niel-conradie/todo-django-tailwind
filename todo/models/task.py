from django.contrib.auth import get_user_model
from django.db import models

from todo.models import DayModel

from utils.models import UUIDModel


CustomUser = get_user_model()


class TaskModel(UUIDModel):
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

    TRUE = True
    FALSE = False
    STATUS_CHOICES = (
        (TRUE, "Active"),
        (FALSE, "Inactive"),
    )
    status = models.BooleanField(
        choices=STATUS_CHOICES,
        default=TRUE,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Task"
        verbose_name_plural = "Tasks for the Day"

    def __str__(self):
        return self.title
