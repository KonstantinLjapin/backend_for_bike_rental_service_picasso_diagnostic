from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BaseBikeSerializer
from .models import Bike, Rent
from users_api.models import CustomUser


class ListBikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema()
    def get(self, request):
        bikes = Bike.objects.filter(fuse=True)
        serializer = BaseBikeSerializer(instance=bikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RentStartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema()
    def post(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        if user.fuse:
            serializer = BaseBikeSerializer(data=request.data)
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'You must end last rent'}, status=status.HTTP_200_OK)


class RentEndView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema()
    def post(self, request):
        bikes = Bike.objects.filter(fuse=True)
        serializer = BaseBikeSerializer(instance=bikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
