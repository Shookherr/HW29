from rest_framework.viewsets import ModelViewSet

from ads.serializers.location import LocationSerializer
from ads.models import Location


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
