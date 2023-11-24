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
