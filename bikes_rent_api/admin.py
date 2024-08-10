from django.contrib import admin
from .models import Rent, History, Bike


@admin.register(Bike)
class CustomUser(admin.ModelAdmin):
    list_display = ('id', 'bike_model', 'fuse')


@admin.register(History)
class CustomUser(admin.ModelAdmin):
    list_display = ('id', 'rent')


@admin.register(Rent)
class CustomUser(admin.ModelAdmin):
    list_display = ('id', 'bike', 'user', 'date')
