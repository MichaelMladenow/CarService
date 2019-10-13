from parts.models import Part, PartGroup
from rest_framework import serializers


class PartGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PartGroup
        fields = ['name']


class PartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Part
        fields = ['name', 'group', 'applicable_cars', 'stock', 'price']

