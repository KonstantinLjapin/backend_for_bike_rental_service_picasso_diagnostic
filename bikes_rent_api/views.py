from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import BaseBikeSerializer
from .models import Bike


class ListBikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        bikes = Bike.objects.filter(fuse=True)
        serializer = BaseBikeSerializer(instance=bikes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
