
from .models import ChAddresses
from rest_framework import serializers


class ChAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = '__all__'
