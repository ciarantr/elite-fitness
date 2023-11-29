from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse

from apps.ecommerce.products.models import Product


class CartTest(TestCase):
    """
    Test cart view & cart functionality
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='@??-=s12345'
        )
        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description',
            price=10.00,
            stock=10,
            slug='test-product',
        )

    def test_CartPageView_auth_user(self):
        # Test that the view url exists at the desired location
        # and returns a 200 response code, uses the correct template & has the
        # expected context data

        self.client.login(username='testuser', password='@??-=s12345')

        response = self.client.get(reverse('cart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

        # test if the context has the expected data
        form = response.context['add_to_wishlist_form']
        self.assertIsNotNone(form)

    def test_AddToCartView(self):
        # Test adding a product to the cart
        # Test message displayed

        product = Product.objects.first()

        response = self.client.post(
            reverse('add_to_cart', kwargs={'item_id': product.pk}),
            {'quantity': '1', 'redirect_url': '/'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn('cart', self.client.session)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         f'Added {product.name} to your cart')

        self.assertEqual(
            self.client.session['cart'][str(product.pk)], 1)

    def test_RemoveFromCartView(self):
        # Test removing a product from the cart
        # Test correct message displayed
        product = Product.objects.first()

        # Add product to cart
        self.client.post(
            reverse('add_to_cart', kwargs={'item_id': product.pk}),
            {'quantity': '1', 'redirect_url': '/'}
        )
        # Remove product from cart
        response = self.client.post(
            reverse('remove_from_cart',
                    kwargs={'item_id': product.pk}),
            {'redirect_path': '/'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertNotIn(str(product.pk), self.client.session['cart'])

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         f'Removed {product.name} from your cart')

    def test_AdjustCartView(self):
        # Test adjusting the quantity of a product in the cart
        # Test correct message displayed
        product = Product.objects.first()

        # Add product to cart
        self.client.post(
            reverse('add_to_cart', kwargs={'item_id': product.pk}),
            {'quantity': '1', 'redirect_url': '/'}
        )

        response = self.client.post(
            reverse('adjust_cart', kwargs={'item_id': product.pk}),
            {'quantity': '2', 'redirect_url': '/'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.client.session['cart'][str(product.pk)], 2)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 2)
        self.assertEqual(str(messages[1]),
                         f'Updated {product.name} quantity to 2')

    def test_AddToCartView_stock(self):
        # Test adding a product more than its stock quantity
        product = Product.objects.first()

        response = self.client.post(
            reverse('add_to_cart', kwargs={'item_id': product.pk}),
            {'quantity': '', 'redirect_url': '/'}
        )

        self.assertEqual(response.status_code, 302)

        messages = list(get_messages(response.wsgi_request))
        print(messages)
        self.assertEqual(len(messages), 1)
        self.assertIn('only have', str(messages[0]))  # stock error message


def test_remove_from_cart_view_exception(self):
    # Test removing a non-existing item from cart
    bad_pk = self.product.pk + 345  # assuming this doesn't exist

    response = self.client.post(
        reverse('remove_from_cart', kwargs={'item_id': bad_pk}),
        {'redirect_path': '/'}
    )

    self.assertEqual(response.status_code, 500)  # error status

    messages = list(get_messages(response.wsgi_request))
    self.assertEqual(len(messages), 1)
    self.assertIn('Error removing item:', str(messages[0]))


def test_adjust_cart_view_zero_quantity(self):
    # Test adjusting cart quantity to 0 (should remove the item)
    # Firstly add a product
    self.client.post(
        reverse('add_to_cart', kwargs={'item_id': self.product.pk}),
        {'quantity': '1', 'redirect_url': '/'}
    )

    # Now try setting quantity to 0
    response = self.client.post(
        reverse('adjust_cart', kwargs={'item_id': self.product.pk}),
        {'quantity': '0', 'redirect_url': '/'}
    )

    self.assertEqual(response.status_code, 302)
    self.assertNotIn(str(self.product.pk), self.client.session['cart'])

    messages = list(get_messages(response.wsgi_request))
    self.assertEqual(len(messages), 2)
    # Check message for removing item due to zero quantity
    self.assertIn('Removed', str(messages[1]))
    self.assertIn('from your cart', str(messages[1]))
