from rest_framework import serializers
from .models import User
import random
from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password_hash"]

    def create(self, validated_data):
        user = User(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"].lower(),
            password_hash=validated_data["password_hash"],
            is_active=False,
            is_verified=False
        )
        user.save()

        code = str(random.randint(100000, 999999))
        user.verification_code = code
        user.save()

        send_mail(
            "Confirm your email",
            f"Your verification code is {code}",
            "fatoumatoutolo@gmail.com",  
            [user.email],
        )

        return user


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")

        if user.verification_code != data["code"]:
            raise serializers.ValidationError("Invalid verification code")

        user.is_verified = True
        user.is_active = True
        user.save()
        return data
