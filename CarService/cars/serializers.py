from cars.models import Car
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['Model', 'Brand', 'License Plate']