from django.shortcuts import render
from rest_framework import viewsets
from .models import ChAddresses
from .serializers import ChNpaSerializer, ChStrNameSerializer, ChCitySerializer, ChStrNrSerializer, ChAddressesSerializer

import requests


class CHNpaView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.values("plz4").distinct()
    serializer_class = ChNpaSerializer
    model = ChAddresses
    filterset_fields = ('plz4',)
    search_fields = ('plz4',)

class CHCityView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.values("gdename").distinct()
    serializer_class = ChCitySerializer
    model = ChAddresses
    filterset_fields = ('plz4', 'gdename',)
    search_fields = ('gdename',)

class CHStrNameView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.values("strname").distinct()
    serializer_class = ChStrNameSerializer
    model = ChAddresses
    filterset_fields = ('plz4','strname',)
    search_fields = ('strname',)

class CHStrNrView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.all()
    serializer_class = ChStrNrSerializer
    model = ChAddresses
    filterset_fields = ('plz4','strname','deinr',)
    search_fields = ('plz4','strname','deinr',)

class CHAddressesView(viewsets.ModelViewSet):
    queryset = ChAddresses.objects.all()
    serializer_class = ChAddressesSerializer
    model = ChAddresses
    filterset_fields = ('plz4','strname','deinr',)
    search_fields = ('strname','deinr','plz4',)
