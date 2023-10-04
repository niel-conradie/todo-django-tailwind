from django.contrib.auth.models import AbstractUser

from utils.models import UUIDModel


class CustomUser(AbstractUser, UUIDModel):
    pass

    def __str__(self):
        return self.username
