from django.test import TestCase

from apps.ecommerce.orders.forms import OrderForm


class TestOrderForm(TestCase):
    """
    Test Order form
    1.Test form fields are explicitly set
    2.Test form fields have correct attributes
    3.Test form is valid with correct data
    4.Test form is invalid with incorrect data
    """

    def setUp(self):
        self.form = OrderForm()

    def test_fields_are_explicit_in_form_metaclass(self):
        self.assertEqual(self.form.Meta.fields,
                         ('full_name', 'email', 'phone_number',
                          'street_address1', 'street_address2',
                          'town_or_city', 'postcode', 'country',
                          'county',))

    def test_full_name_field_has_attrs(self):
        self.assertEqual(
            self.form.fields['full_name'].widget.attrs.get('autofocus'),
            True)
        self.assertEqual(
            self.form.fields['full_name'].widget.attrs.get('class'),
            'stripe-style-input')

        # loop through all fields and test check placholders
        # are all capitalised & have no underscores
        for field in self.form.fields:
            self.assertEqual(
                self.form.fields[field].widget.attrs.get('placeholder'),
                field.replace("_", " ").title())
        # test one label has underscored removed & is capitalised
        self.assertEqual(
            self.form.fields['full_name'].widget.attrs.get('placeholder'),
            'Full Name')

    def test_form_validity(self):
        form = OrderForm(data={
            'full_name': 'John Doe',
            'email': 'john.doe@gmail.com',
            'phone_number': '123456789',
            'street_address1': 'Street 1',
            'street_address2': 'Street 2',
            'town_or_city': 'City',
            'postcode': '12345',
            'country': 'IE',
            'county': 'County'
        })
        self.assertTrue(form.is_valid())

    def test_form_invalidity(self):
        form = OrderForm(data={
            'full_name': '',
            'email': 'john',
            'phone_number': '123456789',
            'street_address1': 'Street 1',
            'street_address2': 'Street 2',
            'town_or_city': 'City',
            'postcode': '12345',
            'country': 'Country',
            'county': 'County'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'],
                         ['This field is required.'])
        self.assertEqual(form.errors['email'],
                         ['Enter a valid email address.'])
