from django.db import models

class Grid(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    data = models.TextField()

