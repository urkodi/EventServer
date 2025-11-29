from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    phoneNumber = serializers.CharField(source="phone_number", allow_null=True)
    profilePicture = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "firstName",
            "lastName",
            "email",
            "phoneNumber",
            "timezone",
            "location",
            "bio",
            "username",
            "profilePicture",
        ]

    def get_profilePicture(self, obj):
        request = self.context.get("request")
        if obj.pfp_path and hasattr(obj.pfp_path, "url"):
            return request.build_absolute_uri(obj.pfp_path.url)
        return None