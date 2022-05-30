from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission, User
from django.db import models
from django.utils import timezone


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username