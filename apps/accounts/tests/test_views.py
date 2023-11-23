from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class ProfileViewTest(TestCase):
    """
    Test the profile view and form
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='@??-=s12345'
        )
        self.login = self.client.login(
            username='testuser',
            password='@??-=s12345',
        )

    def test_view_url_exists_at_desired_location(self):
        # Test that the view url exists at the desired location
        # and returns a 200 response code & uses the correct template
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
