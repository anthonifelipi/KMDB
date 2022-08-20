from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    bio = models.TextField(null=True, blank=True)
    is_critic = models.BooleanField(null=True, blank=True, default=False)
    updated_at = models.DateField(default=datetime.now)

    REQUIRED_FIELDS = ["email", "first_name", "last_name", "birthdate"]


# EOF
