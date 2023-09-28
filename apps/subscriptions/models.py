import uuid

from django.db import models


class Subscription(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text="Required: Please enter your "
                                            "first name.")
    last_name = models.CharField(max_length=100,
                                 help_text="Required: Please enter your last "
                                           "name.")
    email = models.EmailField(max_length=254, unique=True, )
    created = models.DateTimeField(auto_now_add=True, editable=False,)
    updated = models.DateTimeField(auto_now=True)
    confirmation_token = models.UUIDField(default=uuid.uuid4, editable=False,
                                          null=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
