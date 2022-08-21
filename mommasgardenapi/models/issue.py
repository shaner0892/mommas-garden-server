from django.db import models

class Issue(models.Model):

    category = models.ForeignKey("IssueCategory", on_delete=models.CASCADE)
    note = models.CharField(max_length=500)
    date = models.DateField()
    plant = models.ForeignKey("Plant", on_delete=models.CASCADE)
    url = models.CharField(max_length=2000, default="https://i.etsystatic.com/33348027/r/il/ec1edb/3609190565/il_1588xN.3609190565_n82r.jpg")
    solution = models.CharField(max_length=500)