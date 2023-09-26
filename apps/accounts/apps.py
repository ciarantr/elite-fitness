from django.apps import AppConfig
from django.db.models.signals import post_save


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'

    def ready(self):
        from apps.accounts.signals import update_email_address
        post_save.connect(update_email_address, sender='auth.User')
