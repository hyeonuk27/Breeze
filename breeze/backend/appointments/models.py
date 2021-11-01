from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    # id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    datetime = models.DateTimeField()
    middle_place = models.CharField(max_length=50)


class Appointmentplace(models.Model):
    # id = models.IntegerField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='Appointmentplaces')


class Participant(models.Model):
    # id = models.IntegerField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=20)
    address = models.TextField()
    building = models.CharField(max_length=50)
    time = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()