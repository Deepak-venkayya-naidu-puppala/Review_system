from django.db import models

# Create your models here.
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=16)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(models):
        return "Name : {} ".format(models.name)

