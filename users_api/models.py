from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, AbstractUser)


class CustomUser(AbstractUser, PermissionsMixin):

    def __str__(self):
        return self.email
