from rest_framework import serializers

class ReverseGeocodingSerializer(serializers.Serializer):
    latitude = serializers.DecimalField(17,15)
    longitude = serializers.DecimalField(18,15)