
from .models import ChAddresses
from rest_framework_json_api import serializers

class ChAddressesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChAddresses
        fields = '__all__'

#Converts to json
