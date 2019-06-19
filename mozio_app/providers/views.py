from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Provider, ServiceArea
from .serializer import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """
    Create, Update, Delete and Retrieves providers
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = (AllowAny,)


class ServiceAreaViewSet(
        mixins.RetrieveModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        mixins.UpdateModelMixin,
        viewsets.GenericViewSet):
    """
    Create, Update, Delete and Retrieves service areas
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    permission_classes = (AllowAny,)


class ListServiceAreas(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """
        Return a list of all service areas 
        with the given latitude and longitude.
        """
        latitude = float(request.query_params.get('lat', 0))
        longitude = float(request.query_params.get('lng', 0))
        coordinates = [latitude, longitude]
        filtered_service_areas = ServiceArea.objects.filter(coordinates__contains=coordinates)
        service_areas = [{'Name': area.name, 'Price': area.price,
                          'Provider name': area.provider.name} for area in filtered_service_areas]
        return Response(service_areas)
