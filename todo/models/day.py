from django.db import models

from utils.models import UUIDModel


class DayModel(UUIDModel):
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
        verbose_name = "Day"
        verbose_name_plural = "Days of the Week"

    def __str__(self):
        return self.title
