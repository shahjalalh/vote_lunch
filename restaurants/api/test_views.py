from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurants.models import Menu


class MenuTests(APITestCase):

    def test_create_account(self):
        """
        Getting today menu
        """
        url = 'http://0.0.0.0:8000/api/v1/menu/today'
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        