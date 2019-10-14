from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        password = serializers.CharField(write_only=True)
        fields = ['url', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializerWithToken(UserSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    # is this really static?
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

        return token

    class Meta:
        model = User
        fields = ('token', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'write_only': True},
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']