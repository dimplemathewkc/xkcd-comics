import requests
from django.core.management import BaseCommand



import logging

from api.models import Comic

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Load data from xkcd API to DB"

    def handle(self, *args, **options):
        for i in range(1, 5):
            try:
                response = requests.get(f"https://xkcd.com/{i}/info.0.json")
                if not Comic.objects.filter(title=response.json()["title"]).exists():
                    comic = Comic.objects.create(
                        title=response.json()["title"],
                        description=response.json()["alt"],
                        image=response.json()["img"],
                        issue=response.json()["num"],
                        day=response.json()["day"],
                        month=response.json()["month"],
                        year=response.json()["year"],
                    )
                    comic.save()

            except requests.exceptions.RequestException as e:
                logger.error(e)
