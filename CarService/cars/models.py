from django.db import models


class Car(models.Model):
    model         = models.CharField('Model', max_length=30)
    brand         = models.CharField('Brand', max_length=30)
    license_plate = models.CharField('License Plate', max_length=8)