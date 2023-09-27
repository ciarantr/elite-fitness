import json
import time

import stripe
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
from stripe.error import StripeError

from apps.accounts.models import DeliveryDetails
from apps.ecommerce.orders.models import Order, OrderLineItem
from apps.ecommerce.products.models import Product
from core import settings


def _send_confirmation_email(order):
    """Send the user a confirmation email"""
    cust_email = order.email

    subject = render_to_string(
        'emails/confirmation_order_subject.txt',
        {'order': order},
        request=None  # Pass the request context if needed
    )

    # Load the HTML templates using get_template
    html_template = get_template('emails/confirmation_order_body.html')

    # Render the HTML template with the context
    html_body = html_template.render({'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    # Create the email
    email = EmailMultiAlternatives(
        subject,
        body=html_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[cust_email],
    )
    # set the content subtype to html
    email.content_subtype = "html"

    # Send the email
    email.send()


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        try:
            stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        except stripe.error.StripeError as e:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                status=500)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = DeliveryDetails.objects.get(user__username=username)
            if save_info:
                # profile.default_full_name = shipping_details.name
                # profile.default_email = billing_details.email
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            _send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {str(e)}',
                    status=500)
        _send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created '
                    f'order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
