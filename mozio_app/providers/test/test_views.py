import factory


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from mozio_app.providers.models import Provider


class ProviderTest(APITestCase):

    def test_create_provider(self):
        """
        Ensure we can create a new provider object.
        """
        url = reverse('provider-list')
        data_id = factory.Faker('uuid4')
        data = {
            "id": "123123",
            "name": "sample-provider",
            "email": "ddz@gmail.com",
            "phone_number": "11111",
            "language": "English",
            "currency": "US Dollar"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, 'sample-provider')
        self.assertEqual(response.data, {
            "id": "123123",
            "name": "sample-provider",
            "email": "ddz@gmail.com",
            "phone_number": "11111",
            "language": "English",
            "currency": "US Dollar"
        })


class ServiceAreaTest(APITestCase):

    def test_create_service_area(self):
        """
        Ensure we can create a new service area object.
        """
        url = reverse('servicearea-list')
        data = {
            "provider": "f0c9e028-c4cb-41c0-b194-65616e823c77",
            "name": "Sample Service Area",
            "price": 10.0,
            "geojson": {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [-27.421875, 63.35212928507874],
                                    [-11.513671874999998, 63.35212928507874],
                                    [-11.513671874999998, 67.03316279015063],
                                    [-27.421875, 67.03316279015063],
                                    [-27.421875, 63.35212928507874]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [-6.8994140625, 60.50052541051131],
                                    [-13.53515625, 51.645294049305406],
                                    [0.8349609375, 49.83798245308484],
                                    [4.130859375, 52.3755991766591],
                                    [-6.8994140625, 60.50052541051131]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [-6.96533203125, 63.25341156651705],
                                    [-10.08544921875, 61.58549218152362],
                                    [-5.42724609375, 61.05828537037916],
                                    [-4.28466796875, 62.1655019058381],
                                    [-6.96533203125, 63.25341156651705]
                                ]
                            ]
                        }
                    }
                ]
            },
        }
        response = self.client.post(url, data, format='json')
        print(response)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().geojson.get('features').length, 1)
