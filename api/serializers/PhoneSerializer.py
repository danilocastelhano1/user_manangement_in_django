from rest_framework import serializers

from api.models.Phones import Phones


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = (
            'id', 'number', 'area_code', 'country_code'
        )
