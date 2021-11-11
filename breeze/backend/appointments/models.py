from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    datetime = models.DateTimeField()
    middle_place = models.CharField(max_length=50)
    secret_code = models.TextField(default=0)


class Appointmentplace(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='appointment_places')
    name = models.CharField(max_length=20)
    category = models.IntegerField()
    url = models.TextField()


class Participant(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=20)
    time = models.IntegerField()
    barami_type = models.IntegerField()
