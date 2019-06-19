from rest_framework import serializers
from rest_framework.fields import ListField
from .models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = ('id', 'name', 'phone_number', 'language', 'currency', 'email')
        # read_only_fields = ('email', )


# class StringArrayField(ListField):
#     """
#     String representation of an array field.
#     """
#     def to_representation(self, obj):
#         obj = super(StringArrayField, self).to_representation(obj)
#         # convert list to string
#        return ",".join([str(element) for element in obj])

#     def to_internal_value(self, data):
#         data = data.split(",")  # convert string to list
#         return super().to_internal_value(self, data)


class ServiceAreaSerializer(serializers.ModelSerializer):

    # coordinates = StringArrayField()

    class Meta:
        model = ServiceArea
        fields = ('id', 'provider', 'name', 'price', 'geojson')
