import logging

from django.core.management import BaseCommand
from django.utils import timezone

from apps.contacts import models


class Command(BaseCommand):
    help = "Delete animals"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        current_amount = models.Contacts.objects.all().count()
        self.logger.info(f"Current amount of animals: {current_amount}")

        query = models.Contacts.objects

        required_datetime = timezone.now() - timezone.timedelta(
            seconds=20,
        )
        query = (
            query.order_by("creation_date").filter(creation_date__lt=required_datetime).filter(is_auto_generated=True)
        )
        total_amount, details = query.delete()

        self.logger.info(f"Amount of deleted animals : {total_amount}")

        amount_after_generating = models.Contacts.objects.all().count()
        self.logger.info(f"Amount of animals after action: {amount_after_generating}")
