from django.contrib import admin
from django.urls import path
from .views import MenuAPIView, TodayMenuListAPIView, VoteMenuAPIView, WinnerAPIView


urlpatterns = [
    path('create', MenuAPIView.as_view(), name='create'),
    path('today', TodayMenuListAPIView.as_view(), name='today-menu'),
    path('vote', VoteMenuAPIView.as_view(), name='vote-menu'),
    path('winner', WinnerAPIView.as_view(), name='menu-winner'),
]
