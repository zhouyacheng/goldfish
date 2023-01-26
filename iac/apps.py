from django.apps import AppConfig


class IacConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'iac'

    def ready(self):
        super(IacConfig,self).ready()
        from common.extensions import BearerTokenAuthenticationScheme
