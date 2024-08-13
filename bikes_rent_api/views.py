from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.serializers import ValidationError
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
    def put(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        if user.fuse:
            bike_serializer = BaseBikeSerializer(data=request.data)
            try:
                bike_serializer.is_valid(raise_exception=True)
            except ValidationError as e:
                #ErrorDetail(string='bike with this bike model already exists.', code='unique'
                if e.default_code == 'unique':
                    return Response({'message': f'{bike_serializer.data}'}, status=status.HTTP_200_OK)
        return Response({'message': 'You must end last rent'}, status=status.HTTP_412_PRECONDITION_FAILED)


class RentEndView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema()
    def post(self, request):
        bikes = Bike.objects.filter(fuse=True)
        serializer = BaseBikeSerializer(instance=bikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
