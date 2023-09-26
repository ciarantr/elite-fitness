from allauth.account.models import EmailAddress
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
# Update user email address & allauth email address
def update_email_address(sender, instance=None, created=False, **kwargs):
    if not created:  # If user is not created
        email_address_instance = EmailAddress.objects.filter(
            user=instance).first()
        if email_address_instance:
            email_address_instance.email = instance.email
            email_address_instance.save()
