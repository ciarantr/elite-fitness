from django.contrib.auth.models import User
from django.test import TestCase


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

