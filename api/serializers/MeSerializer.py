from rest_framework import serializers

from api.models.User import User

from api.serializers.PhoneSerializer import PhoneSerializer


class MeSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True, read_only=False)

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password', 'phones'
        )
