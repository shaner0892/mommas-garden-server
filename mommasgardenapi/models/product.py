from django.db import models

class Product(models.Model):

    plant = models.ForeignKey("Plant", on_delete=models.CASCADE)
    harvest_date = models.DateField()
    url = models.CharField(max_length=2000, default="https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg")
    