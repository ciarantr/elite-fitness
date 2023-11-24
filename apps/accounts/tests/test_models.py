from django.contrib.auth.models import User
from django.test import TestCase

from ..models import DeliveryDetails


class DeliveryDetailsModelTest(TestCase):
    """
    Test DeliveryDetails model
    1.Set up a user and DeliveryDetails instance with default values
    2.Test DeliveryDetails model
    3.Test DeliveryDetails username
    3.Test DeliveryDetails content
    4.Test DeliveryDetails content updated

    Note: Test depends on django signals in accounts/models.py
    when a user is created a deliverydetails table is populated in db
    with the django user or updated if a user is already created

    """

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(username='testuser',
                                            email='johndoe@example.com',
                                            password='12345$%£$$%@@@ji')
        # Additional attributes for DeliveryDetails are set here
        cls.user.deliverydetails.default_full_name = "John Doe"
        cls.user.deliverydetails.default_email = "johndoe@example.com"
        cls.user.deliverydetails.default_phone_number = "1234567890"
        cls.user.deliverydetails.default_country = "Ireland"
        cls.user.deliverydetails.default_postcode = "12345"
        cls.user.deliverydetails.default_town_or_city = "Dublin"
        cls.user.deliverydetails.default_street_address1 = "123 street"
        cls.user.deliverydetails.default_street_address2 = "Apartment 456"
        cls.user.deliverydetails.default_county = "Dublin County"
        cls.user.deliverydetails.save()

    def test_delivery_details_creation(self):
        delivery_details = DeliveryDetails.objects.get(id=1)
        self.assertEqual(str(delivery_details), 'testuser')

    def test_delivery_details_username(self):
        delivery_details = DeliveryDetails.objects.get(id=1)
        expected_username = "testuser"

        self.assertEqual(str(delivery_details.user.username),
                         expected_username)

    def test_delivery_details_content(self):
        delivery_details = DeliveryDetails.objects.get(id=1)
        expected_full_name = "John Doe"
        expected_email = "johndoe@example.com"
        expected_phone_number = "1234567890"
        expected_country = "Ireland"
        expected_postcode = "12345"
        expected_town_or_city = "Dublin"
        expected_street_address1 = "123 street"
        expected_street_address2 = "Apartment 456"
        expected_county = "Dublin County"

        self.assertEqual(delivery_details.default_full_name,
                         expected_full_name)
        self.assertEqual(delivery_details.default_email, expected_email)
        self.assertEqual(delivery_details.default_phone_number,
                         expected_phone_number)
        self.assertEqual(delivery_details.default_country,
                         expected_country)
        self.assertEqual(delivery_details.default_postcode,
                         expected_postcode)
        self.assertEqual(delivery_details.default_town_or_city,
                         expected_town_or_city)
        self.assertEqual(delivery_details.default_street_address1,
                         expected_street_address1)
        self.assertEqual(delivery_details.default_street_address2,
                         expected_street_address2)
        self.assertEqual(delivery_details.default_county,
                         expected_county)

    def test_delivery_details_content_updated(self):
        # change all the details and test values are updated
        self.user.deliverydetails.default_full_name = "Jane Doe"
        self.user.deliverydetails.default_email = "janedoe@example.com"
        self.user.deliverydetails.default_phone_number = "0987654321"
        self.user.deliverydetails.default_country = "GB"
        self.user.deliverydetails.default_postcode = "54321"
        self.user.deliverydetails.default_town_or_city = "London"
        self.user.deliverydetails.default_street_address1 = "456 street"
        self.user.deliverydetails.default_street_address2 = "Apartment 123"
        self.user.deliverydetails.default_county = "Greater London"
        self.user.deliverydetails.save()

        delivery_details = DeliveryDetails.objects.get(id=1)
        expected_full_name_update = "Jane Doe"
        expected_email_update = "janedoe@example.com"
        expected_phone_number_update = "0987654321"
        expected_country_update = "GB"
        expected_postcode_update = "54321"
        expected_town_or_city_update = "London"
        expected_street_address1_update = "456 street"
        expected_street_address2_update = "Apartment 123"
        expected_county_update = "Greater London"

        self.assertEqual(delivery_details.default_full_name,
                         expected_full_name_update)
        self.assertEqual(delivery_details.default_email, expected_email_update)
        self.assertEqual(delivery_details.default_phone_number,
                         expected_phone_number_update)
        self.assertEqual(delivery_details.default_country,
                         expected_country_update)
        self.assertEqual(delivery_details.default_postcode,
                         expected_postcode_update)
        self.assertEqual(delivery_details.default_town_or_city,
                         expected_town_or_city_update)
        self.assertEqual(delivery_details.default_street_address1,
                         expected_street_address1_update)
        self.assertEqual(delivery_details.default_street_address2,
                         expected_street_address2_update)
        self.assertEqual(delivery_details.default_county,
                         expected_county_update)

