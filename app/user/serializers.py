from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as translate_language

from rest_framework import serializers


class userSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "name")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validate_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validate_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attributes):
        """Validate and authenticate the user"""
        email = attributes.get("email")
        password = attributes.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password
        )

        if not user:
            message = translate_language(
                "Unable to authenticate with provided credentials"
            )
            raise serializers.ValidationError(message, code="authentication")

        attributes["user"] = user
        return attributes
