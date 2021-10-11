
from .serializers import CustomUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from custom_users.models import CustomUser
from rest_framework import status


class CustomUserAPIView(APIView):
    """Create new employee or restaurent.
    """

    def username_exists(self, username):

        if CustomUser.objects.filter(username=username).exists():
            return True
    
        return False

    def post(self, request, format=None):
        """Create a employee or a restaurant. Both employee and restaurant 
           can not contain same data.

        Args:
            request ([POST]): http://0.0.0.0:8000/api/v1/users/create
            Form Fields:
                'username': 'john'
                'first_name': 'John'
                'last_name': 'Doe'
                'email': 'john.doe@gmail.com'
                'password': 'super-secret-pass'
                'employee': True
                'restaurant': False

        Returns:
            {
                "id": 5,
                "username": "john"
            }
            or,
            {
                "error": "Invalid data"
            }
        """

        # check 'request.data' has employee or restaurent True
        user_data = request.data

        if user_data.get('employee') != user_data.get('restaurant'):

            if self.username_exists(user_data.get('username')):
                return Response({'error': 'Username is already in use'}, 
                status=status.HTTP_400_BAD_REQUEST)
            else:

                serializer = CustomUserSerializer(data=request.data)
                
                if serializer.is_valid():
                    serializer.save()

                    user_data = {
                        'id': serializer.data.get('id'),
                        'username': serializer.data.get('username'),
                    }
                    return Response(user_data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid data'}, 
            status=status.HTTP_400_BAD_REQUEST)
