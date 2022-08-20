from django.db import models
from django.contrib.auth.models import User

class Gardener(models.Model):

    bio = models.CharField(max_length=300)
    url = models.CharField(max_length=1000)
    location = models.CharField(max_length=100)
    planting_zone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
