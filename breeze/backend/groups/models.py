from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=20)


class Groupmember(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groupmembers')
    name = models.CharField(max_length=20)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()