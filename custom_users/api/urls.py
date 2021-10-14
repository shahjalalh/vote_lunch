"""Custom User Urls
"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CustomUserAPIView, LogoutAPIView

urlpatterns = [
    path('register', CustomUserAPIView.as_view(), name='register'),
    path('login', obtain_auth_token, name="auth_token"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
]
