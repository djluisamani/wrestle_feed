from django.db import models

class Promoters(models.Model):
    name = models.CharField(max_length=255)
    hq_city = models.CharField(max_length=255)
    year_founded = models.IntegerField()
