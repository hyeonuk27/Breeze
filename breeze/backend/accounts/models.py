from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)