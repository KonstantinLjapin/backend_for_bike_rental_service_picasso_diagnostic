from django.db import models
from users_api.models import CustomUser


class Bike(models.Model):
    bike_model = models.CharField(max_length=30, unique=True)
    fuse = models.BooleanField(default=False)

    def __str__(self):
        return "Bike " + str(self.bike_model)


class Rent(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Rent " + str(self.user) + str(self.bike)


class History(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE)
