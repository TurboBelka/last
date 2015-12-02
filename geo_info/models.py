from django.db import models


class GeoInfo(models.Model):
    ip = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    user_agent = models.TextField()
    headers = models.TextField()
    date = models.DateTimeField()
