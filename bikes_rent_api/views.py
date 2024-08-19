from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BaseBikeSerializer, BaseRentSerializer
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
            bike_serializer.is_valid()
            if "bike_model" in bike_serializer.errors.keys():
                if "bike with this bike model already exists." in bike_serializer.errors.get("bike_model"):
                    bike: Bike = Bike.objects.get(id=request.data["id"])
                    rent: Rent = Rent(bike=bike, user=user)
                    rent.save()
                    return Response({'message': f'{rent.date_start}'}, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'You must end last rent'}, status=status.HTTP_412_PRECONDITION_FAILED)


class RentEndView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    @swagger_auto_schema()
    def put(self, request):
        user = CustomUser.objects.get(id=request.user.id)
        bike_serializer = BaseBikeSerializer(data=request.data)
        bike_serializer.is_valid()
        if "bike_model" in bike_serializer.errors.keys():
            if "bike with this bike model already exists." in bike_serializer.errors.get("bike_model"):
                Bike.objects.filter(bike_model=bike_serializer.data.get('bike_model')).update(fuse=True)
                user.fuse = True
                user.save(update_fields=["fuse"])
                bike = Bike.objects.get(bike_model=bike_serializer.data.get('bike_model'))
                return Response({'message': f'{bike.bike_model}'}, status=status.HTTP_202_ACCEPTED)
        return Response({'message': 'You must end last rent'}, status=status.HTTP_412_PRECONDITION_FAILED)
