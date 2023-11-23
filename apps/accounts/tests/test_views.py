from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import Client, TestCase
from django.urls import reverse

from ..models import DeliveryDetails


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

    def test_form_valid(self):
        # Test that the form is valid and the user profile details are updated
        # Test that the correct message is displayed
        # Assuming form fields for `UserUpdateForm`
        # are 'username', 'email', 'first_name', and 'last_name'
        # Note: form used django auth User model

        response = self.client.post(reverse('profile'), {
            'username': 'newusername',
            'email': 'user@gmail.com',
            'first_name': 'newfirstname',
            'last_name': 'newlastname',
        }
                                    )
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.email, 'user@gmail.com')
        self.assertEqual(self.user.first_name, 'newfirstname')
        self.assertEqual(self.user.last_name, 'newlastname')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Profile updated successfully')


