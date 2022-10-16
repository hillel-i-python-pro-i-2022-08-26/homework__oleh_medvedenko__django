from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    birthday = models.CharField(max_length=255)

    is_auto_generated = models.BooleanField(default=False)

    creation_date = models.DateTimeField(auto_now_add=True)
    edition_date = models.DateTimeField(auto_now=True)

    group = models.ForeignKey(
        Group,
        related_name="contacts",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self) -> list[str]:
        return f"{self.name}{self.phone_number}{self.birthday}{self.creation_date}{self.edition_date}".splitlines()

    __repr__ = __str__
