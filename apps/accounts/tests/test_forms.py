from django.contrib.auth.models import User
from django.test import TestCase

from ..forms import (UserUpdateForm)


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

