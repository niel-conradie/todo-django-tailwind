from django.contrib.auth.models import AbstractUser

from utils.models import ModelUUID


class CustomUser(AbstractUser, ModelUUID):
    pass

    def __str__(self):
        return self.username
