from django.db.models import Model, UUIDField
from django.utils.translation import gettext_lazy as _

import uuid


class UUIDModel(Model):
    """
    A Django model representing a database table with a primary key field of type UUID.

    Parameters:
    - Model (class): The model that adds a UUID field to the model.

    Fields:
    - id (UUIDField): The primary key field of the UUIDModel class.

    Class:
    - Meta: Provides metadata for the TaskModel class in Django.
    """

    id = UUIDField(
        _("id"),
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        """
        Provides metadata for the UUIDModel class in Django.

        Fields:
        - abstract (boolean): Specifies if the UUIDModel class should be treated as an abstract model.
        """

        abstract = True
