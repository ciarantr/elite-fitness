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