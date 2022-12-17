import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


def get_avatar_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"users/user/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class User(AbstractUser):
    avatar = models.ImageField(
        max_length=255,
        null=True,
        blank=True,
        upload_to=get_avatar_path,
    )
