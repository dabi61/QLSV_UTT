from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=250)
    population = models.PositiveIntegerField()