from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=255, unique=True, default= '')
    code = models.CharField(max_length=255, unique=True, default= '')

    class Meta:
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=255, default= '')
    capital = models.CharField(max_length=255, default= '')
    code = models.CharField(max_length=255, unique=True, default= '')
    population = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    continent = models.ForeignKey(Continent, related_name="countries")

    class Meta:
        ordering = ['name']
