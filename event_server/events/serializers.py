from rest_framework import serializers
from .models import Event, EventUsers

class EventSerializer(serializers.ModelSerializer):
    imageUrl = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__" 

    def get_imageUrl(self, obj):
        if obj.image_path:
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image_path.url)
        return None


class EventUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventUsers
        fields = '__all__'
        
