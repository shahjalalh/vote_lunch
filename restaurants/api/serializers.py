"""Restaurant menu serializer
"""
from rest_framework import serializers

from restaurants.models import Menu


class TodayMenuSerializer(serializers.ModelSerializer):
    """Menu serializer.
    """
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
