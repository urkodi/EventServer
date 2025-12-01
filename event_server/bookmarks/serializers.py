from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    event_title = serializers.CharField(source="event.title", read_only=True)

    class Meta:
        model = Bookmark
        fields = ["id", "event", "event_title", "saved_at"]
        read_only_fields = ["saved_at"]
