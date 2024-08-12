from django.contrib import admin
from .models import Rent, Bike


@admin.register(Bike)
class CustomBikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike_model', 'fuse')


@admin.register(Rent)
class CustomRentAdmin(admin.ModelAdmin):
    list_display = ("id", "date_start", "date_end", "bike", "user")
