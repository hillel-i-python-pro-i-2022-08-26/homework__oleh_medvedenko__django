import uuid

from django.db import models
from django.urls import reverse_lazy


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/image/{instance.pk}/{uuid.uuid4()}/image.{extension}"


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True, default=None)
    is_auto_generated = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    group = models.ForeignKey(
        Group,
        related_name="contacts",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse_lazy("post", kwargs={"post_id": self.pk})

    def get_update_url(self):
        return reverse_lazy("contacts:update_contact", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return "\n".join(f"{self.name}")

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
