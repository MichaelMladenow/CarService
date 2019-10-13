from django.db import models


class PartGroup(models.Model):
    name = models.CharField('Group', max_length=30)


class Part(models.Model):
    name = models.CharField('Name', max_length=30)
    group = models.ForeignKey(PartGroup)
    stock = models.IntegerField('Stock')