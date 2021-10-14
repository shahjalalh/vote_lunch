"""Custom User Test
"""
from rest_framework import status
from rest_framework.test import APITestCase

from custom_users.models import CustomUser


class CustomUserTests(APITestCase):
    """Custom User API test
    """

    def test_create_account(self):
        """Ensure we can create a new account object.
        """
        url = 'http://0.0.0.0:8000/api/v1/users/register'

        data = {'username': 'dab',
                'first_name': 'dab',
                'last_name': 'Doe',
                'email': 'dab.doe@gmail.com',
                'password': 'super-secret-pass',
                'employee': True,
                'restaurant': False
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username, 'dab')
        