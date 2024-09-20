from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login, logout
from .serializers import BaseUserSerializer, ProfileSerializer
from drf_yasg import openapi


class RegisterView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    serializer_class = BaseUserSerializer

    @swagger_auto_schema(method='post')
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    @swagger_auto_schema(method='post')
    def post(self, request: Request, *args, **kwargs) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(method='post')
    def post(self, request: Request, *args, **kwargs) -> Response:
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)


class UserProfileView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ProfileSerializer

    @swagger_auto_schema(method='post')
    def get(self, request: Request, *args, **kwargs) -> Response:
        user = request.user
        serializer = ProfileSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
