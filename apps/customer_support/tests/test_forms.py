from django.test import TestCase

from ..forms import ContactForm


class TestContactForm(TestCase):
    """
    Test the ContactForm
    1. Test that the form is valid
    2. Test that the form is invalid
    3. Test that the form is invalid when email is invalid
    4. Test that the form is invalid when first_name is invalid
    5. Test that the form is valid when phone_number is not provided
    6. Test that the form is invalid when min/max length is violated
    """

    def test_form_valid(self):
        # Test that the form is valid
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone_number': '+1234567890',
            'message': 'Hello, this is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_email(self):
        # Test that the form is invalid when email is invalid
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'not_an_email',
            'phone_number': '+1234567890',
            'message': 'Hello, this is a test message.'
        })
        self.assertFalse(form.is_valid())

    def test_form_invalid_first_name(self):
        # Test that the form is invalid when first_name is invalid
        form = ContactForm(data={
            'first_name': 'John@',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone_number': '+1234567890',
            'message': 'Hello, this is a test message.'
        })
        self.assertFalse(form.is_valid())

    def test_form_phone_number_optional(self):
        # Test that the form is valid when phone_number is not provided
        form = ContactForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'message': 'Hello, this is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_form_min_max_length_violation(self):
        # Test that the form is invalid when min/max length is violated
        form = ContactForm(data={
            'first_name': 'J',    # Length is less than min_length
            'last_name': 'D' * 51,  # Length is more than max_length
            'email': 'john@example.com',
            'phone_number': '+1234567890',
            'message': 'Short'  # Length is less than min_length
        })
        self.assertFalse(form.is_valid())
