from django.db import models

class IssueCategory(models.Model):

    type = models.CharField(max_length=50)