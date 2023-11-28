import json

from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from apps.customer_support.forms import ContactForm
from core import settings


class AboutView(TemplateView):
    """
    This view handles the display of the about page
    """
    template_name = 'about.html'
    title = 'About Us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('customer_support:contact')
    title = 'Contact Us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def form_valid(self, form):
        """
        Send email to customer support and user.
        """
        full_name = f'{form.cleaned_data["first_name"]} ' \
                    f'{form.cleaned_data["last_name"]}'
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']

        send_mail(
            subject=render_to_string('email/contact_email_subject.txt'),
            message=render_to_string('email/contact_email_body.txt', {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'message': message,
            }),

            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL,
                            form.cleaned_data['email']],

        )
        messages.success(self.request,
                         f'Thank you '
                         f'{form.cleaned_data["first_name"]} for contacting '
                         f'us.'
                         f' We will get back to you shortly.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, 'Please correct the errors below.')
        return super().form_invalid(form)


class FaqsView(TemplateView):
    """
    This view handles the display of the faqs page
    """
    template_name = 'faqs.html'
    title = 'FAQs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Import JSON data from file
        with open('apps/customer_support/static/data/faqs.json', 'r') as file:
            faqs = json.load(file)

        context['title'] = self.title
        context['faqs'] = faqs
        return context


class PrivacyPolicyView(TemplateView):
    """
    This view handles the display of the privacy policy page
    """

    template_name = 'privacy_policy.html'
    title = 'Privacy Policy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ShippingAndInformationView(TemplateView):
    """
    This view handles the display of the shipping and information page
    """
    template_name = 'shipping_and_information.html'
    title = 'Shipping & Information'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['free_delivery_threshold'] = settings.FREE_DELIVERY_THRESHOLD
        return context


class TermsAndConditionsView(TemplateView):
    """
    This view handles the display of the terms and conditions page
    """
    template_name = 'terms_and_conditions.html'
    title = 'Terms & Conditions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
