from django.db import models


class Brand(models.Model):
    name = models.CharField('Brand', max_length=30)


class Model(models.Model):
    name  = models.CharField('Model', max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Car(models.Model):
    model         = models.ForeignKey(Model, on_delete=models.CASCADE)
    license_plate = models.CharField('License Plate', max_length=8)