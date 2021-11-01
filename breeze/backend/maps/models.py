from django.db import models
from django.conf import settings

class Place(models.Model):
    # id = models.IntegerField(primary_key=True)
    category_num = models.IntegerField()
    name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    kakao_url = models.TextField()
    review = models.IntegerField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    tag = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()