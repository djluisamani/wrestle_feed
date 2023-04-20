from django.db import models
from promoters.models import Promoter
from wrestlers.models import Wrestler

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE)
    wrestler = models.ForeignKey(Wrestler, on_delete=models.CASCADE, null=True)