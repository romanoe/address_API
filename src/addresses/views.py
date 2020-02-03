from django.shortcuts import render
from rest_framework import viewsets
from .models import ChAddresses
from .serializers import ChNpaSerializer, ChStrNameSerializer, ChCitySerializer

import requests


class CHNpaView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.values("plz4").distinct()
    serializer_class = ChNpaSerializer
    model = ChAddresses
    filterset_fields = ('plz4',)


class CHCityView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.values("gdename").distinct()
    serializer_class = ChCitySerializer
    model = ChAddresses
    filterset_fields = ('plz4', 'gdename',)

class CHStrNameView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.all()
    serializer_class = ChStrNameSerializer
    model = ChAddresses
    filterset_fields = ('plz4','strname_de',)
