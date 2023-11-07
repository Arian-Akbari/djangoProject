from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
