from django.db import models


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(default="", blank=True)


class Reading(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    date = models.DateField()
    reading = models.FloatField()
