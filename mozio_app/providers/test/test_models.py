from django.test import TestCase
from mozio_app.providers.models import Provider, ServiceArea


default_geojson = {
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
}


class ProviderModelTest(TestCase):

    def create_provider(self, name="sample name",
                        phone_number="328746823648", language="English",
                        currency="$", email="sample@gmail.com"):
        return Provider.objects.create(name=name, phone_number=phone_number,
                                       language=language, currency=currency,
                                       email=email)

    def test_provider_creation(self):
        p = self.create_provider()
        self.assertTrue(isinstance(p, Provider))
        self.assertEqual(p.name, 'sample name')


class ServiceAreaModelTest(TestCase):

    def create_service_area(self, provider="f0c9e028-c4cb-41c0-b194-65616e823c77",
                            name="Sample Service Area", price=20.0, geojson=default_geojson):
        return ServiceArea.objects.create(provider=name, name=phone_number,
                                          price=language, geojson=geojson)

    def test_service_area_creation(self):
        sa = self.create_service_area()
        self.assertTrue(isinstance(sa, ServiceArea))
        self.assertEqual(sa.provider.pk, "f0c9e028-c4cb-41c0-b194-65616e823c77")
