

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.models(email=email, **extra_fields)
        user.set_password()
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50, blank=True, )



