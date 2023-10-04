from django.db import models

from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
)

from utils.models import UUIDModel


class PrivacyModel(
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
    UUIDModel,
):
    body = models.TextField()

    class Meta:
        ordering = ("-modified",)
        verbose_name = "Privacy"
        verbose_name_plural = "Privacy"
