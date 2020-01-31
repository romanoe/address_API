
# Create your views here.
from .models import ChAddresses
from .serializers import ChAddressesSerializer
from rest_framework import viewsets


class CHAddressesView(viewsets.ModelViewSet):
    serializer_class = ChAddressesSerializer
    model = ChAddresses
    queryset = ChAddresses.objects.all()
