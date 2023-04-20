from django.db import models
from promoters.models import Promoter

class Wrestlers(models.Model):
    wrestler_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    division = models.CharField(max_length=255, choices=(('male', 'Male'), ('female', 'Female')), null=True)
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE)