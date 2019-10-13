from repairs.models import RepairService, RepairServiceGroup
from rest_framework import serializers


class RepairServiceGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairServiceGroup
        fields = ['name']


class RepairServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairService
        fields = ['name', 'group', 'applicable_cars', 'price']

