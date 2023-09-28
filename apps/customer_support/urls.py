from django.urls import path

from apps.customer_support.views import (
    AboutView)

app_name = 'customer_support'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]
