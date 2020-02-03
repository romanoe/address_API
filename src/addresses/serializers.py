
from .models import ChAddresses
from rest_framework import serializers


class ChNpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = ('plz4',)

class ChCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = ('gdename',)

class ChStrNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = ('strname',)

class ChStrNrSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChAddresses
        fields = ('deinr',)
