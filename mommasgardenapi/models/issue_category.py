from django.db import models

class IssueCategory(models.Model):

    issue = models.CharField(max_length=50)