"""Test for restaurant menu
"""
from rest_framework import status
from rest_framework.test import APITestCase


class MenuTests(APITestCase):
    """Menu Test Class
    """

    def test_create_account(self):
        """Getting today menu
        """
        url = 'http://0.0.0.0:8000/api/v1/menu/today'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        