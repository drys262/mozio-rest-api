import uuid


from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@python_2_unicode_compatible
class Provider(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=55)
    language = models.CharField(max_length=55)
    currency = models.CharField(max_length=55)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ServiceArea(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    geojson = JSONField()
    coordinates = ArrayField(
        ArrayField(models.FloatField()),
        blank=True,
        null=True
    )
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=ServiceArea)
def add_coordinates(sender, instance=None, created=False, **kwargs):
    features = instance.geojson.get('features')
    all_coordinates = []
    for feature in features:
        feature_type = feature.get('type')
        geometry = feature.get('geometry')
        coordinates = geometry.get('coordinates')[0]
        for coordinate in coordinates:
            all_coordinates.append(coordinate)

    instance.coordinates = all_coordinates
