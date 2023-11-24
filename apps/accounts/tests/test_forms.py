from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import (CustomUserCreationForm, CustomerDeliveryForm,
                     UserUpdateForm)


class TestUserUpdateForm(TestCase):
    """
    Test the UserUpdateForm
    Note: form used django auth User model
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
        )

    def test_valid_data(self):
        form = UserUpdateForm({
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'New',
            'last_name': 'newuser',
        }, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserUpdateForm({}, instance=self.user)
        self.assertFalse(form.is_valid())

    def test_invalid_data_missing_username(self):
        form = UserUpdateForm({
            'username': '',
            'email': '',
            'first_name': 'New',
            'last_name': 'User',
        }, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'],
                            ['This field is required.'])
        self.assertEqual(form.errors['email'],
                            ['This field is required.'])


class TestCustomUserCreationForm(TestCase):
    """
    Test the CustomUserCreationForm
    Note: form used django auth UserCreationForm model
    """

    def test_valid_data(self):
        form = CustomUserCreationForm({
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        # The Form is invalid because password1 and password2 do not match
        # and the username is not provided
        form = CustomUserCreationForm({
            'username': 'newuser',
            'password1': 'testpassword123',
            'password2': 'testpassword1234',
        })
        self.assertFalse(form.is_valid())


class TestCustomerDeliveryForm(TestCase):
    """
    Test the CustomerDeliveryForm
    """

    def test_customer_delivery_form_is_valid(self):
        form = CustomerDeliveryForm({
            'default_full_name': 'John Doe',
            'default_email': 'johndoe@example.com',
            'default_phone_number': '1234567890',
            'default_country': 'IE',
            'default_postcode': '90210',
            'default_town_or_city': 'Dublin',
            'default_street_address1': '123 Main St',
            'default_street_address2': 'Apt 4B',
            'default_county': 'County Dublin',
        })
        self.assertTrue(form.is_valid())

    def test_customer_delivery_form_is_invalid(self):
        form = CustomerDeliveryForm({})
        self.assertFalse(form.is_valid())

    def test_customer_delivery_form_missing_required_fields(self):
        form = CustomerDeliveryForm({
            'default_full_name': '',
            'default_email': '',
            'default_phone_number': '1234567890',
            'default_country': '',
            'default_postcode': '90210',
            'default_town_or_city': '',
            'default_street_address1': '',
            'default_street_address2': 'Apt 4B',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['default_full_name'],
                         ['This field is required.'])
        self.assertEqual(form.errors['default_email'],
                         ['This field is required.'])
        self.assertEqual(form.errors['default_country'],
                         ['This field is required.'])
        self.assertEqual(form.errors['default_town_or_city'],
                         ['This field is required.'])
        self.assertEqual(form.errors['default_street_address1'],
                         ['This field is required.'])
