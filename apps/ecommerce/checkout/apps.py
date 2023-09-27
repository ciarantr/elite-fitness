from django.apps import AppConfig
from django.db.models.signals import post_save


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ecommerce.checkout'

    def ready(self):
        from apps.ecommerce.checkout.signals import update_on_delete, \
            update_on_save
        from apps.ecommerce.orders.models import OrderLineItem
        post_save.connect(update_on_save, sender=OrderLineItem)
        post_save.connect(update_on_delete, sender=OrderLineItem)
