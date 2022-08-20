from django.db import models

class PlantType(models.Model):

    type = models.CharField(max_length=20)
    