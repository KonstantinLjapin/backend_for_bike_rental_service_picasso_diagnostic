from django.db import models
from users_api.models import CustomUser


class Bike(models.Model):
    bike_model = models.CharField(max_length=30, unique=True)
    fuse = models.BooleanField(default=True)

    def __str__(self):
        return "Bike " + str(self.bike_model)


class Rent(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='rents', on_delete=models.CASCADE)
    date_start = models.DateTimeField(auto_now_add=True, blank=True)
    date_end = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "Rent " + str(self.user) + " " + str(self.bike)
