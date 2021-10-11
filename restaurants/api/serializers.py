from rest_framework import serializers
from restaurants.models import Menu
from custom_users.api.serializers import CustomUserSerializer


class TodayMenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='full_name'
     )

    class Meta:
        model = Menu
        fields = [
            'id',
            'name',
            'restaurant',
            'detail',
            'price',
            'created_date'
        ]
