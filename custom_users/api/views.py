from .serializers import CustomUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from custom_users.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CustomUserAPIView(APIView):
    """Create new employee or restaurent.
    """

    def username_exists(self, username):
        """Check if the username already exists.
        """

        if CustomUser.objects.filter(username=username).exists():
            return True
    
        return False

    def post(self, request, format=None):
        """A single API to create a employee or a restaurant. 
        Both employee and restaurant can not contain same data.

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
        logger.error("Invalid data!!")
        return Response({'error': 'Invalid data'}, 
            status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    """Logout new employee or restaurent.
    """

    def post(self, request, format=None):
        """Logout the user

        Args:
            request ([POST]): http://0.0.0.0:8000/api/v1/users/logout
            Form Fields:
                'token': '0066f17d9199a0ae62db97a8b3051efc612128a7'

        Returns:
            Status: 205 Reset Content
        """

        try:
            user_token = request.data.get("token", None)
            token = Token.objects.get(key=user_token)
            token.delete()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            logger.error("Bad request!!")
            return Response(status=status.HTTP_400_BAD_REQUEST)