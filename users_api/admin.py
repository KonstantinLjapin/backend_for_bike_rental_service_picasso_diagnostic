from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'password')


