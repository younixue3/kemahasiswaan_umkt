from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission, User
from django.db import models
from django.utils import timezone
import uuid

class User(AbstractUser):
    uniid = models.UUIDField(default=uuid.uuid4(), editable=False)
