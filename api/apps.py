from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        from api.service import get_comic_data
        logger.info("Starting comic data loader")
        get_comic_data()
