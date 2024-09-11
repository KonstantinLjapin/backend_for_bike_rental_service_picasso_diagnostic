from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users_api.models import CustomUser


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account-list')
        data = {"username": "ivan",
                "password": "qwerty",
                "email": "ivan@example.com"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().name, 'DabApps')
