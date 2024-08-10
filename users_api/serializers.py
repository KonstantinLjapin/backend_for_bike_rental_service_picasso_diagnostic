from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from bikes_rent_api.serializers import BaseRentSerializer
UserModel = get_user_model()


class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", )


class ProfileSerializer(serializers.ModelSerializer):
    rents = BaseRentSerializer(instance='rents', many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    class Meta:
        Depth = 1
        model = UserModel
        fields = ("id", "username", "email", "rents")
