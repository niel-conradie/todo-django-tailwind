from django.db import models

from django_extensions.db.models import (
    ActivatorModel,
    TimeStampedModel,
    TitleSlugDescriptionModel,
)

from utils.models import ModelUUID


class Privacy(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, ModelUUID):
    body = models.CharField(
        max_length=200,
    )

    class Meta:
        verbose_name_plural = "Privacies"
