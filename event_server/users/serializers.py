from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # Exposed camelCase fields (output + input)
    firstName = serializers.CharField(source="first_name", required=False)
    lastName = serializers.CharField(source="last_name", required=False)
    phoneNumber = serializers.CharField(source="phone_number", required=False)

    # Hidden write-only snake_case fields for updates
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    phone_number = serializers.CharField(required=False, write_only=True)

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

            # REQUIRED to allow updates to work:
            "first_name",
            "last_name",
            "phone_number",
        ]

    def get_profilePicture(self, obj):
        request = self.context.get("request")
        if obj.pfp_path and request:
            return request.build_absolute_uri(obj.pfp_path.url)
        return None

    def to_internal_value(self, data):
        print("RAW INPUT:", data)

        mapped = data.copy()

        camel_to_snake = {
            "firstName": "first_name",
            "lastName": "last_name",
            "phoneNumber": "phone_number",
            "profilePicture": "pfp_path",
        }

        for camel, snake in camel_to_snake.items():
            if camel in data:
                mapped[snake] = data[camel]

        print("MAPPED INPUT:", mapped)
        return super().to_internal_value(mapped)

    def update(self, instance, validated_data):
        print("VALIDATED DATA:", validated_data)
        return super().update(instance, validated_data)