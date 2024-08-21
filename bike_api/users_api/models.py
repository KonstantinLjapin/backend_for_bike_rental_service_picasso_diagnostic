from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, AbstractUser)


class CustomUser(AbstractUser, PermissionsMixin):
    fuse = models.BooleanField(default=True)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.email
