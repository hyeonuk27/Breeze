from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    datetime = models.DateTimeField()
    middle_place = models.CharField(max_length=50)