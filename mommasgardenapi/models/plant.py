from django.db import models

class Plant(models.Model):

    species = models.CharField(max_length=50)
    date_planted = models.DateField()
    producing = models.BooleanField()
    type = models.ForeignKey("PlantType", on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, default="https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg")
    gardener = models.ForeignKey("Gardener", on_delete=models.CASCADE)