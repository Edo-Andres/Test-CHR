from django.db import models

# Create your models here.

class BikeSantiago(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    href = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    stations = models.IntegerField()


class EstacionBicicletas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    uid = models.IntegerField()

    bike_santiago = models.ForeignKey(BikeSantiago, on_delete=models.CASCADE)
