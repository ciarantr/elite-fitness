from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import TemplateView

from apps.ecommerce.products.models import Product
from apps.subscriptions.forms import SubscriptionForm
from apps.subscriptions.models import Subscription
from core import settings


def _send_confirmation_email(form, confirmation_link):
    """Send the user a confirmation email"""
    email = form.email
    first_name = form.first_name

    subject = render_to_string(
        'emails/confirmation_subscription_subject.txt',
    )
    # Render the template to a string and escape the HTML content
    body = render_to_string(
        'emails/confirmation_subscription_body.html',
        {'first_name': first_name,
         'confirmation_link': confirmation_link},
    )
    send_mail(
        subject=subject,
        message=False,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        html_message=body,
        fail_silently=False,
    )


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            category__name__icontains='supplements')[:3]
        # Assign image to each product
        for product in context['products']:
            product.image = product.images.first()
        # Add a subscription form
        context['form'] = SubscriptionForm()

        return context

    def post(self, request, *args, **kwargs):
        """
        Save the subscription form if valid & user email does not exist.
        Send confirmation email to user.
        """
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if not Subscription.objects.filter(email=email).exists():
                form.save()
                confirmation_link = request.build_absolute_uri(
                    reverse('confirm-signup',
                            kwargs={
                                'confirmation_token':
                                    form.instance.confirmation_token
                            }
                            )
                )

                _send_confirmation_email(form.instance, confirmation_link)

        messages.info(request,
                      "Please check your email for to confirm subscription.")
        return redirect('home')
