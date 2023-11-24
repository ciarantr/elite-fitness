import json
from unittest.mock import mock_open, patch

from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse


class AboutViewTest(TestCase):
    """
    Test the AboutView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """

    def setUp(self):
        self.client = Client()

    def test_get_context_data(self):
        response = self.client.get(reverse('customer_support:about'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

        self.assertIn('title', response.context_data)
        self.assertEqual(response.context_data['title'], 'About Us')


class ContactViewTest(TestCase):
    """
    Test the ContactView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    3. Test that the form is valid and mail is sent
    4. Test that the form is invalid
    """

    def setUp(self):
        self.client = Client()

        self.valid_data = {
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@gmail.com",
            "phone_number": "1234567890",
            "message": "Test message"
        }

    def test_get_context_data(self):
        response = self.client.get(reverse('customer_support:contact'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

        self.assertIn('title', response.context_data)
        self.assertEqual(response.context_data['title'], 'Contact Us')

    # Test a when form is valid & mail is sent
    @patch('apps.customer_support.views.send_mail')
    def test_form_valid(self, mock_send_mail):
        response = self.client.post(reverse('customer_support:contact'),
                                    data=self.valid_data)

        # Test that a success message has been added to messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Thank you Test for contacting us. '
                         'We will get back to you shortly.')

        # Test sending of mail
        self.assertTrue(mock_send_mail.called)

    # Test a when form is invalid
    def test_form_invalid(self):
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not an email address'

        response = self.client.post(reverse('customer_support:contact'),
                                    data=invalid_data)

        # Test that an error message has been added to messages
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Please correct the errors below.')


class FaqsViewTest(TestCase):
    """
    Test the FaqsView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """

    def setUp(self):
        self.client = Client()

    @patch('builtins.open',
           new_callable=mock_open,
           read_data='[{"q":"Question", "a":"Answer"}]')
    def test_get_context_data(self, mock_file):
        response = self.client.get(reverse('customer_support:faqs'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        #  test url uses the correct template
        self.assertTemplateUsed(response, 'faqs.html')

        # Ensure faqs data in the context, you can add more specific
        # checks about its content
        self.assertIn('faqs', response.context_data)

        # Check that 'faqs' context data is the same type object as mocked data
        self.assertEqual(json.loads(mock_file().read()),
                         response.context_data['faqs'])


class PrivacyPolicyViewTest(TestCase):
    """
    Test the PrivacyPolicyView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """

    def setUp(self):
        self.client = Client()

    def test_get_context_data(self):
        response = self.client.get(reverse('customer_support:privacy-policy'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy_policy.html')

        self.assertIn('title', response.context_data)
        self.assertEqual(response.context_data['title'],
                         'Privacy Policy')


class ShippingAndInformationViewTest(TestCase):
    """
    Test the ShippingAndInformationView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """

    def setUp(self):
        self.client = Client()

    def test_get_context_data(self):
        response = self.client.get(
            reverse('customer_support:shipping-and-information'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'shipping_and_information.html')

        self.assertIn('title', response.context_data)
        self.assertIn('free_delivery_threshold', response.context_data)
        self.assertEqual(response.context_data['title'],
                         'Shipping & Information')
        self.assertEqual(response.context_data['free_delivery_threshold'],
                         50)


class TermsAndConditionsViewTest(TestCase):
    """
    Test the TermsAndConditionsView
    1. Test that the view url exists at the desired location
    and returns a 200 response code & uses the correct template
    2. Test that the view returns the correct context data
    """
    def setUp(self):
        self.client = Client()

    def test_get_context_data(self):
        response = self.client.get(
            reverse('customer_support:terms-and-conditions'))

        # Ensure status code 200 i.e., OK
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'terms_and_conditions.html')

        self.assertIn('title', response.context_data)
        self.assertEqual(response.context_data['title'],
                         'Terms & Conditions')

