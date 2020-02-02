from django.shortcuts import render
from rest_framework import viewsets
from .models import ChAddresses
from .serializers import ChAddressesSerializer


class CHAddressesView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.all()
    serializer_class = ChAddressesSerializer
    model = ChAddresses
    
