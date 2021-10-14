"""Custom User Serializer
"""
from rest_framework import serializers

from custom_users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Custom User Serializer
    """

    def create(self, validated_data):
        """Create user with password in ModelSerializer.
        """

        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'employee',
            'restaurant',
            'password'
        ]
