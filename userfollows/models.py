from django.db import models
from promoters.models import Promoter
from wrestlers.models import Wrestler
from django.contrib.auth.models import User

class UserFollows(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wrestler = models.ForeignKey(Wrestler, on_delete=models.CASCADE)
    promoter = models.ForeignKey(Promoter, on_delete=models.CASCADE)