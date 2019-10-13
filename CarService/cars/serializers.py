from cars.models import Brand, Model, Car, UserCar
from rest_framework import serializers


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Model
        fields = ['name', 'brand']


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ['model']


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserCar
        fields = ['car', 'model']
