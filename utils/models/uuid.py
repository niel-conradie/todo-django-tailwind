import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelUUID(models.Model):
    """
    We use this in every db entry.
    """

    id = models.UUIDField(
        _("id"),
        primary_key=True,
        default=uuid.uuid4,
    )

    class Meta:
        abstract = True
