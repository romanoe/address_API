
from .models import ChAddresses
from rest_framework import serializers


class ChAddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = ('egid','plz4','gdename','strname_de','geom')
