from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    description = models.TextField()
    justification = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    area_hectares = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=128)

class State(models.Model):
    name = models.CharField(max_length=128)
    iso = models.CharField(max_length=2)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=128)