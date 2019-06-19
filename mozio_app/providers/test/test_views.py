from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Provider


class ProviderTest(APITestCase):
    """
    Ensure we can create a new provider object.
    """
    url = reverse('provider-list')
    # data = {'name': 'DabApps'}
    data = {
        "name": "DabApps",
        "email": "ddz@gmail.com",
        "phone_number": "11111",
        "language": "English",
        "currency": "US Dollar"
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Provider.objects.count(), 1)
    self.assertEqual(Provider.objects.get().name, 'DabApps')
