from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source="event.name", read_only=True)

    class Meta:
        model = Ticket
        fields = ["id", "event", "event_name", "quantity", "booked_at"]
