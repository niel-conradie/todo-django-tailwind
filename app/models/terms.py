from django.db import models

from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
)

from utils.models import UUIDModel


class TermsModel(
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
    UUIDModel,
):
    body = models.TextField()

    class Meta:
        ordering = ("-modified",)
        verbose_name = "Terms of Service"
        verbose_name_plural = "Terms of Service"
