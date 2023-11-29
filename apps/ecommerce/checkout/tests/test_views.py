from unittest.mock import patch

from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpResponse
from django.test import Client, RequestFactory, TestCase

from apps.ecommerce.orders.models import Order
from apps.ecommerce.products.models import Product
from ..views import (CheckoutSuccessView, CheckoutView)


class MockStripePaymentIntent:
    def __init__(self, client_secret):
        self.client_secret = client_secret

    def create(self, *args, **kwargs):
        return self


class CheckoutViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = CheckoutView.as_view()
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            stock=10,
            slug='test-product',
        )
        self.data = {
            'full_name': 'Test Name',
            'email': 'testemail@test.com',
            'phone_number': '+1234567890',
            'country': 'Country',
            'postcode': '123456',
            'town_or_city': 'City',
            'street_address1': 'Street 1',
            'street_address2': 'Street 2',
            'county': 'County',
            'client_secret': 'random_secret_1234'
        }

    def add_middleware_to_request(self, request, middleware_class):
        middleware = middleware_class(lambda req: HttpResponse())
        middleware.process_request(request)
        request.session.save()

    # @patch('stripe.PaymentIntent')
    # def test_get_request(self, MockPaymentIntent):
    #     # Session for cart
    #     session = self.client.session
    #     session['cart'] = {str(self.product.id): 1}
    #     session.save()
    #
    #     # Setup mock Stripe response
    #     intent = MockStripePaymentIntent('random_secret')
    #     MockPaymentIntent.create.return_value = intent
    #
    #     request = self.factory.get('/checkout/')
    #     self.add_middleware_to_request(request, SessionMiddleware)
    #     self.add_middleware_to_request(request, MessageMiddleware)
    #     request.session = session
    #     request.user = AnonymousUser()
    #
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, 200)

    @patch('stripe.PaymentIntent')
    def test_post_request(self, MockPaymentIntent):
        session = self.client.session
        request = self.factory.post('/checkout/', data=self.data)
        self.add_middleware_to_request(request, SessionMiddleware)
        self.add_middleware_to_request(request, MessageMiddleware)
        response = self.view(request)
        session['save_info'] = True
        self.assertEqual(response.status_code, 302)


class CheckoutSuccessViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.view = CheckoutSuccessView.as_view()

    def test_get_request(self):
        order = Order.objects.create(
            full_name='Test Name',
            email='test@ymail.com',
            phone_number='+1234567890',
            country='Country',
            postcode='123456',
            town_or_city='City',
            street_address1='Street 1',
            street_address2='Street 2',
            county='County',
            order_total=10.00,
            stripe_pid='random_secret_1234'
        )
        request = self.client.get('/checkout/success/{order.order_number}/')
        request.user = AnonymousUser()
        # Add session to the request

        kwargs = {'order_number': order.order_number}
        response = self.view(request, **kwargs)
        self.assertEqual(response.status_code, 200)

# class CacheCheckoutDataViewTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.view = CacheCheckoutDataView.as_view()
#         self.data = {
#             'full_name': 'Test Name',
#             'email': '
