from collections.abc import Iterator
from datetime import datetime

from faker import Faker

from apps.contacts import models

fake = Faker()


def generate_contacts(amount: int = 10) -> Iterator[models.Contacts]:
    for _ in range(amount):
        yield models.Contacts(
            name=fake.name(),
            phone_number=fake.phone_number(),
            birthday=fake.date_between_dates(date_start=datetime(1940, 1, 1), date_end=datetime(2010, 12, 12)),
        )
