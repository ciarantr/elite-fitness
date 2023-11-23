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


class OrderProfileViewTest(TestCase):
    """
    Test the order profile view and form
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.login = self.client.login(username='testuser',
                                       password='12345')
        self.user.deliverydetails.default_full_name = "John Doe"
        self.user.deliverydetails.save()
        self.delivery_details_obj = DeliveryDetails.objects.get(id=1)

    def test_view_url_exists_at_desired_location(self):
        # Test that the view url exists at the desired location
        # and returns a 200 response code & uses the correct template
        response = self.client.get(reverse('order_information'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delivery_information.html')

    def test_form_valid(self):
        # Assuming form fields for `CustomerDeliveryForm` are 'address',
        # 'city', and 'zipcode'
        response = self.client.post(
            reverse('order_information'),
            {
                'default_full_name': 'jane doe',
                'default_email': 'janedoe@gmail.com',
                'default_phone_number': '1234567890',
                'default_street_address1': 'new address',
                'default_street_address2': 'new address 2',
                'default_country': 'IE',
                'default_town_or_city': 'new city',
                'default_postcode': 'new zip'
            }
        )
        self.delivery_details_obj.refresh_from_db()
        self.assertEqual(self.delivery_details_obj.default_full_name,
                         'jane doe')
        self.assertEqual(self.delivery_details_obj.default_email,
                         'janedoe@gmail.com')
        self.assertEqual(self.delivery_details_obj.default_phone_number,
                         '1234567890')
        self.assertEqual(self.delivery_details_obj.default_country,
                            'IE')
        self.assertEqual(self.delivery_details_obj.default_street_address1,
                         'new address')
        self.assertEqual(self.delivery_details_obj.default_street_address2,
                         'new address 2')
        self.assertEqual(self.delivery_details_obj.default_town_or_city,
                         'new city')
        self.assertEqual(self.delivery_details_obj.default_postcode,
                         'new zip')

        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Delivery information updated successfully')
