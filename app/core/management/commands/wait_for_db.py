import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        # wite a message on the screen
        self.stdout.write("waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    "Database not availeble, waiting 1 second..."
                )
                # try to connect every one second to the dataBase
                # tell it gets available
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Available"))
