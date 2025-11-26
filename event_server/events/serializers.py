from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("name", "description", "timestamp", "address", "longitude", "latitude", "owner_id")
        read_only_fields = ("owner_id",)