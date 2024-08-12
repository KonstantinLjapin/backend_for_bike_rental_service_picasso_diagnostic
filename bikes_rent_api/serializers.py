from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Bike, Rent


class BaseBikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bike
        fields = ("id", "bike_model", "fuse")


class BaseRentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rent
        fields = ("id", "date_start", "date_end", "bike", "user")
