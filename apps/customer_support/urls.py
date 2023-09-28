from django.urls import path

from apps.customer_support.views import (
    AboutView, ContactView, FaqsView, PrivacyPolicyView)

app_name = 'customer_support'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faqs/', FaqsView.as_view(), name='faqs'),
    path('privacy-policy/', PrivacyPolicyView.as_view(),
         name='privacy-policy'),
]
