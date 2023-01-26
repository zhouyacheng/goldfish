from django.apps import AppConfig
from django.conf import settings
from mongoengine import connect


class CmdbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cmdb'

    def ready(self):
        connect(**settings.MONGODB_DATABASES)
