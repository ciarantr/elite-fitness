from django.urls import path

from apps.customer_support.views import (
    AboutView, ContactView)

app_name = 'customer_support'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
