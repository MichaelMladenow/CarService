from django.db import models
from cars.models import Car


class PartGroup(models.Model):
    name = models.CharField('Group', max_length=30)


class Part(models.Model):
    name = models.CharField('Name', max_length=30)
    applicable_cars = models.ManyToManyField(Car)
    group = models.ForeignKey(PartGroup)
    stock = models.IntegerField('Stock')
    price = models.IntegerField('Price')
