from django.urls import path

from apps.customer_support.views import (
    AboutView, ContactView, FaqsView)

app_name = 'customer_support'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faqs/', FaqsView.as_view(), name='faqs'),
]
