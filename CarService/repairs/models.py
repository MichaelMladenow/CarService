from django.db import models
from cars.models import Car


class RepairServiceGroup(models.Model):
    name = models.CharField('Group', max_length=30)


class RepairService(models.Model):
    name = models.CharField('Name', max_length=30)
    applicable_cars = models.ManyToManyField(Car)
    group = models.ForeignKey(RepairServiceGroup, on_delete=models.CASCADE)
    price = models.IntegerField('Price')
