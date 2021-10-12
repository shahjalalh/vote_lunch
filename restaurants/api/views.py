from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from custom_users.models import CustomUser
from restaurants.models import Menu
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from .serializers import TodayMenuSerializer
from datetime import datetime, timedelta
import time


class MenuAPIView(APIView):

    def post(self, request, format=None):

        # check the token is for valid user
        try:
            token = request.headers.get('Authorization').split(" ")[-1]
            user_id = Token.objects.get(key=token).user_id
            user = CustomUser.objects.get(id=user_id)

            if user.restaurant:
                """only restaurant can create menu
                """
                menu_data = request.data

                created_menu = Menu.objects.create(
                    name = menu_data.get('name'),
                    restaurant = user,
                    detail = menu_data.get('detail'),
                    price = menu_data.get('price')
                )

                menu = {
                    'id': created_menu.id,
                    'name': created_menu.name,
                    'created_date': created_menu.created_date,
                }
                return Response(menu, status=status.HTTP_201_CREATED)
                
            else:
                return Response({'error': 'Not a restaurant.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid user.'}, 
                status=status.HTTP_400_BAD_REQUEST)
    
 
class TodayMenuListAPIView(generics.ListAPIView):
    serializer_class = TodayMenuSerializer

    def get_queryset(self):
        """
        This view should return a list of all the menu
        for current date.
        """
        today = time.strftime("%Y-%m-%d")
        return Menu.objects.filter(created_date=today)


class VoteMenuAPIView(APIView):

    def post(self, request, format=None):
        # check the token is for valid user
        try:
            token = request.headers.get('Authorization').split(" ")[-1]
            user_id = Token.objects.get(key=token).user_id
            user = CustomUser.objects.get(id=user_id)

            if user.employee:
                """only employee can vote on menu
                """
                menu_data = request.data

                menu = Menu.objects.get(
                    id = menu_data.get('id')
                )
                
                menu.votes = menu.votes + 1
                menu.save()

                response_data = {
                    'id': menu.id,
                    'name': menu.name,
                    'created_date': menu.created_date,
                    'votes': menu.votes
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
                
            else:
                return Response({'error': 'Not an employee.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid user.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        except Menu.DoesNotExist:
            return Response({'error': 'Invalid menu.'}, 
                status=status.HTTP_400_BAD_REQUEST)


class WinnerAPIView(APIView):

    def get(self, request, format=None):

        try:
            token = request.headers.get('Authorization').split(" ")[-1]
            user_id = Token.objects.get(key=token).user_id
            user = CustomUser.objects.get(id=user_id)

            if user.employee:
                """only employee can see the winner restaurant
                """
                menu_data = request.data

                today = datetime.today().strftime("%Y-%m-%d")
                today_winner = Menu.objects.filter(created_date=today).order_by('-votes')

                end_date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
                start_date = (datetime.today() - timedelta(days=3)).strftime("%Y-%m-%d")

                last_3_winners = Menu.objects.filter(created_date__range=[start_date, end_date]).order_by('-votes')[:3]

                same_winner = False

                for menu in last_3_winners:
                    if menu.restaurant == today_winner.first().restaurant:
                        same_winner = True
                    else:
                        same_winner = False

                if not same_winner:
                    today_winner = today_winner.first().restaurant
                else:
                    today_winner = today_winner[1].restaurant

                response_data = {
                    'id': today_winner.id,
                    'name': today_winner.full_name,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
                
            else:
                return Response({'error': 'Not an employee.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token.'}, 
                status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid user.'}, 
                status=status.HTTP_400_BAD_REQUEST)