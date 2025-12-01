from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(source="event.title", read_only=True)  # use 'title' or your actual field
    qr_code_url = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ["id", "event", "event_name", "quantity", "qr_code_url", "booked_at"]

    def get_qr_code_url(self, obj):
        request = self.context.get("request")
        if obj.qr_code and request:
            return request.build_absolute_uri(obj.qr_code.url)
        return None
