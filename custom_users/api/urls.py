from django.contrib import admin
from django.urls import path
from .views import CustomUserAPIView, LogoutAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register', CustomUserAPIView.as_view(), name='register'),
    path('login', obtain_auth_token, name="auth_token"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
]
