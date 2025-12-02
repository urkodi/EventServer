from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "event",
            "event_title",
            "event_image",
            "stars",
            "description",
        ]
