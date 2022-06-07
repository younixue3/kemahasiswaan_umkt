from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission, User
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    uniid = models.CharField(max_length=25)
    full_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return '{uniid}-{name}'.format(uniid=self.uniid, name=self.full_name)