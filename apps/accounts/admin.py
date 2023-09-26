from django.contrib import admin

from .models import DeliveryDetails


@admin.register(DeliveryDetails)
class CustomerProfileAdmin(admin.ModelAdmin):

    list_display = ('user',
                    'default_phone_number',
                    'default_email',
                    'default_country')

    ordering = ('user',)
