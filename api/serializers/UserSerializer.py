from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from api.models.Phones import Phones
from api.models.User import User

from api.serializers.PhoneSerializer import PhoneSerializer

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=False)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password', 'phones'
        )

    def create(self, validated_data):
        if 'password' in validated_data:
            new_pass = make_password(validated_data['password'])
            validated_data['password'] = new_pass

        if 'phones' in validated_data:
            phones = validated_data['phones']
            validated_data.pop('phones')

            user = super(UserSerializer, self).create(validated_data)
            for phone in phones:
                phone = Phones.objects.create(**phone)
                user.phones.add(phone)

            return user

    def to_representation(self, instance):
        payload = api_settings.JWT_PAYLOAD_HANDLER(instance)
        token = {
            'token': api_settings.JWT_ENCODE_HANDLER(payload),
            'user': instance
        }

        data = super(UserSerializer, self).to_representation(instance=instance)
        data['token'] = token['token']

        data.pop('id')
        data.pop('first_name')
        data.pop('last_name')
        data.pop('email')
        data.pop('password')
        data.pop('phones')

        return data
