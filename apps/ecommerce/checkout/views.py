import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import DetailView

from apps.accounts.forms import CustomerDeliveryForm
from apps.accounts.models import DeliveryDetails
from apps.ecommerce.cart.context_processors import cart_processor
from apps.ecommerce.orders.forms import OrderForm
from apps.ecommerce.orders.models import Order, OrderLineItem
from apps.ecommerce.products.models import Product


class CheckoutView(View):
    def get(self, request, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the "
                                    "moment")
            return redirect(reverse('products'))

        current_cart = cart_processor(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = DeliveryDetails.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except DeliveryDetails.DoesNotExist:
                order_form = OrderForm()

        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. '
                                      'Did you '
                                      'forget to set it in your environment?')

        template = 'checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in "
                        "our database."
                        "Please call us for assistance!")
                                   )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            request.session['from_checkout'] = True
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an error with your form. '
                           'Please double check your information.')
            return self.get(request)


class CheckoutSuccessView(DetailView):
    model = Order
    template_name = 'checkout_success.html'
    context_object_name = 'order'

    def get_object(self, queryset=None):
        """Get the Order object based on order_number."""
        order_number = self.kwargs.get('order_number')
        return get_object_or_404(Order, order_number=order_number)

    def dispatch(self, request, *args, **kwargs):
        save_info = self.request.session.get('save_info')
        order_number = self.kwargs.get('order_number')
        order = get_object_or_404(Order, order_number=order_number)
        order_email = Order.objects.get(order_number=order_number).email

        if self.request.session.pop('from_checkout', False):
            if request.user.is_authenticated:
                profile = DeliveryDetails.objects.get(user=request.user)
                order.user_profile = profile
                order.save()

                if save_info:
                    profile_data = {
                        'default_full_name': order.full_name,
                        'default_email': order.email,
                        'default_phone_number': order.phone_number,
                        'default_country': order.country,
                        'default_postcode': order.postcode,
                        'default_town_or_city': order.town_or_city,
                        'default_street_address1': order.street_address1,
                        'default_street_address2': order.street_address2,
                        'default_county': order.county,
                    }
                    user_profile_form = CustomerDeliveryForm(profile_data,
                                                             instance=profile)
                    if user_profile_form.is_valid():
                        user_profile_form.save()
            else:
                messages.info(request, "Order placed as guest.")

            messages.success(request,
                             f'Order successfully processed! Your order '
                             f'number is {order_number}. A confirmation '
                             f'email will be sent to {order_email}.')

            if 'cart' in request.session:
                del request.session['cart']
        else:
            if request.user.is_authenticated:
                messages.error(request,
                               f"""Please view your past order history 
                                                in your profile order details
                                                section.
                                                """)
            else:
                messages.error(request,
                               'Please login to view past orders.'
                               )
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)


class CacheCheckoutDataView(View):
    """ A view to cache checkout data"""

    @method_decorator(require_POST)
    def dispatch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            pid = data['client_secret'].split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'cart': json.dumps(request.session.get('cart', {})),
                'save_info': data['save_info'],
                'username': request.user,
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, 'Sorry, your payment cannot be \
                        processed right now. Please try again later.')
            return HttpResponse(content=e, status=400)
