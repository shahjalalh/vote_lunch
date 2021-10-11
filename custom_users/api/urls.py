from django.contrib import admin
from django.urls import path
from .views import CustomUserAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('create', CustomUserAPIView.as_view(), name='create'),
    path('token', obtain_auth_token, name="auth_token")
]