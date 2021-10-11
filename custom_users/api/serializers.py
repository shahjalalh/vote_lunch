from rest_framework import serializers
from custom_users.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        
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
