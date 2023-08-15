from django.contrib import admin

from apps.subscriptions.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'created', 'updated',
                    'is_verified')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created',)
    ordering = ('-created',)
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
    fieldsets = (
        ('Subscription Details', {
            'fields': ('email', 'first_name', 'last_name', 'is_verified')
        }),
        ('Meta data', {
            'fields': ('created', 'updated')
        }),
    )
