from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'event', 'user']   
        read_only_fields = ['user'] 
