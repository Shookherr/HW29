from rest_framework.serializers import ModelSerializer

from ads.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
