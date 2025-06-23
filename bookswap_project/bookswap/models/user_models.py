from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
